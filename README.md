# Collision-Counter

A collision is represented by a tuple of a real number, an integer, and another real number. The tuple (t, i, x) represents a collision happening at time t between objects i and i + 1 at location x. Given a list of masses, a list of initial positions, and a list of initial velocities, each having the same size n, the goal is to enumerate the resulting collisions in a chronological order. Ties between collisions happening at the same time are broken from left to right. For example for i < i′, if at time t, object i collides with i + 1 at location x, and i′ collides with i′ + 1 at location x′, then the collision (t, i, x) must precede (t, i′, x′).
Assumption - The input is such that no more than 2 objects collide at the same time and the same place.
The Python function listCollisions that takes the following five arguments:
1. M: a list of positive floats, where M[i] is the mass of the i’th object,
2. x: a sorted list of floats, where x[i] is the initial position of the i’th object,
3. v: a list of floats, where v[i] is the initial velocity of the i’th object,
4. m: a non-negative integer,
5. T: a non-negative float,
and returns a list of collisions in chronological order that ends as soon as the first m collisions happen or time reaches T (whichever earlier). If the input results in fewer than m collisions and the last collision happens before time T, the list returned will contain all collisions in chronological order. Each collision is represented by a 3-tuple, with the t and x values of collisions rounded to 4 decimal digits.

Time Complexity - O(n + m log n) - Linear in the number of collisions and logarithmic in the number of objects.
