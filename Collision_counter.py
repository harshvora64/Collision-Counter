import math

def round4(x):
    return x

class Point():
    """Point class to store points(objects)
    It stores the mass, position, index, velocity of each object"""
    def __init__(self,i,m,x,v):
        self._index=i
        self._mass=m
        self._position=x
        self._velocity=v

    def m(self):
        return self._mass
    def v(self):
        return self._velocity
    def x(self):
        return self._position
    def i(self):
        return self._index
    
    def update_v(self,v):               # update velocity
        self._velocity = v
    def update_x(self,x):               # update position
        self._position = x
    def update(self,T):                 # update the position to the position after time T (x+=v*T)
        self._position += T* self.v()

    def collide(P1,P2):                 # to update the velocity of two colliding points
        m1=P1.m()
        m2=P2.m()
        v1=P1.v()
        v2=P2.v()
        P2.update_v((2*m1*v1)/(m1+m2)-((m1-m2)*v2)/(m1+m2))
        P1.update_v(((m1-m2)*v1)/(m1+m2)+(2*m2*v2)/(m1+m2))

class Collision():
    """class Collision, whose object stores:
    the time of collision between two objects ( i an i+1)
    the position x where the collision happens
    the 'key' which is the list of [time,index] to compare them for sorting in the minheap
    and 'location' which is the position of the object in the heap list"""
    def __init__(self,P1,P2):
        x1=P1.x()
        x2=P2.x()
        self._time=(x2-x1)/(P1.v()-P2.v()) if P1.v() != P2.v() else math.inf
        m1=P1.m()
        m2=P2.m()
        self._x = x1+self._time*P1.v()
        if self._time<0 or x1>x2:
            self._time=math.inf
        self._i=P1.i()
        self._key=[self._time,self._i]
        self._location=self._i

    def key(self):
        return self._key
    def location(self):
        return self._location
    def set_location(self,l):
        self._location=l
    def update(self,T):
        self._time += T
        self._key[0]=self._time
    def t(self):
        return self._time
    def x(self):
        return self._x
    def i(self):
        return self._i

class MinHeap():
    def __init__(self,entries,collisions):
        l=len(entries)
        self._heap=entries
        self._collisions=collisions
        
        j=l-1
        while(j>=0):
            self.heap_down(j)
            j-=1



    def heap_down(self,location):
        j=location*2+1
        l=len(self._heap)
        while j<l:
            hloc=self._heap[location].key()
            hj=self._heap[j].key()
            if j+1<l:
                hj1 = self._heap[j+1].key()
            else:
                hj1=[math.inf,math.inf]
            if hloc<min(hj,hj1):
                break
            else:
                k = j if hj<hj1 else j+1
                self._heap[location],self._heap[k]=self._heap[k],self._heap[location]
                self._heap[location].set_location(location)
                self._heap[k].set_location(k)
                self._collisions[self._heap[location]._key[1]].set_location(location)
                self._collisions[self._heap[k]._key[1]].set_location(k)
                location = k
                j=location*2+1
    
    def heap_up(self,location):
        j=(location-1)//2
        l=len(self._heap)
        while j>=0:
            hloc=self._heap[location].key()
            hj=self._heap[j].key()
            if hloc>hj:
                break
            else:
                self._heap[location],self._heap[j]=self._heap[j],self._heap[location]
                self._heap[location].set_location(location)
                self._heap[j].set_location(j)
                self._collisions[self._heap[location]._key[1]].set_location(location)
                self._collisions[self._heap[j]._key[1]].set_location(j)
                location = j
                j=(location-1)//2
    

    def reorder(self,new,location):
        o=self._heap[location]
        o._x=new._x
        o._time=new._time
        o._key[0]=new._key[0]
        self.heap_up(location)
        self.heap_down(location)

    def extract_min(self):
        return self._heap[0]

def listCollisions(M,x,v,m,t):
    ans=[]
    time=0
    inf=math.inf
    no_of_collisions=0
    points=[Point(i,M[i],x[i],v[i]) for i in range(len(M))]
    collisions = [Collision(points[i],points[i+1]) for i in range(len(M)-1)]
    entries = [Collision(points[i],points[i+1]) for i in range(len(M)-1)]
    heap = MinHeap(entries,collisions)


    while(time<=t and no_of_collisions<=m):
        collision=heap.extract_min()
        i=collision._key[1]
        T=collision.t()
        time=T
        if time>t:
            break
        no_of_collisions+=1
        if no_of_collisions>m:
            break
        a=(round4(T),collision.i(),round4(collision.x()))
        ans.append(a)
        tx=ans[-1][2]
        points[i].collide(points[i+1])
        points[i].update_x(tx-points[i].v()*T)
        points[i+1].update_x(tx-points[i+1].v()*T)
        collisions[i].update(inf)
        heap.reorder(collisions[i],collisions[i].location())

            
        if i!=0:
            c=Collision(points[i-1],points[i])
            loc=collisions[i-1].location()
            c.set_location(loc)
            heap.reorder(c,loc)
            
        if i!=len(M)-2:
            c=Collision(points[i+1],points[i+2])
            loc=collisions[i+1].location()
            c.set_location(loc)
            heap.reorder(c,loc)
    return(ans)
