# Solving linear equation systems
After the equations have been discretized [[Finite difference method]], we can then solve it.
![[Pasted image 20220531093428.png]]
![[Pasted image 20220531093441.png]]
$$
A \phi = Q
$$
Where A is the matrix of coefficients. This is a sparse matrix. Note that the higher the order, the less sparse the matrix is.
$\phi$ is the unknowns. This is a vector.
$Q$ is the constants. This can be a souce/sink and so on.
So we have this system of linear algebraic equations that we want to solve.

The methods falls into 2  categories:
1) **Direct methods** 
	- These are analytical so they are (almost always) exact
	- But are generally more expensive
2) **Iterative methods**
	- These are the most commonly used
	- The are generally much less expensive
	- But don't give the exacta solution (iteration error)
	- Dont always converge 

## Direct methods

### [[Gauss elimination]]
This is one way to solve the system.  We do something to the A matrix, so we can solve for U.
The steps are:
1) Forward elimination - Here we try yo get it to be a upper triangular matrix
2) Backwards substitution.
But this is very computational expensive!
approx $N^3$ of operations. 

### [[LU decomposition]]
This is a variation of [[Gauss elimination]]
We split the A matrix in a L and U matrix, where $A = LU$
L is a lower diagonal matrix, with a diagonal of ones.

Advantage of LU Factorization can be performed without knowledge of Q (Q not affected)
Suitable when the system should be solved many times with same A but different Q
LU decomposition still as expensive as Gauss elimination

### [[TDMA]]
If we have a tri-diagonal matrix, the cost of [[Gauss elimination]] method reduces to order **N** instead of $N^3$

Note that tri-diagonal means that we only have 3 elements in the row of the matrix.

## Iterative methods
Generally much less expensive then direct methods
BUT they are not exact, and they dont always converge!

### General idea

So the idea is that instead of calculating the result directedly, we can do it iteratively.
$$
A \phi = Q
$$
First we have an initial guess $\phi^0 \rightarrow \phi_1$, where $\phi_1$ is the first iteration.
For the n'th iteration we have: $\phi^n \rightarrow \phi^{n+1}$.
At the end we have that: $\phi^m \approx \phi$, where $\phi$ is the exact solution of $A\phi=Q$

We define the **iteration error** as:
$$\epsilon^n = \text{exact } \phi - \text{current } \phi 
$$
Note that this value cannot be calculated unless the exact solution is known!

**Residual**
$$
\rho^n = Q - A \phi^n
$$
This should be zero, from the boundary conditions.
We can also express it as:
$$
\rho^n = A ( \text{exact } \phi - \text{current } \phi )
$$
**Correction**
$$
\delta^n = \text{current } \phi - \text{previous } \phi
$$
$$
\delta^n = \phi^{n+1}-\phi^n
$$
This is the difference between the current and previous value of $\phi$

### [[Jacobi method]]
For the Jacobi method, we use the old values to calculate the new.
Jacobi method in general has a small convergence speed and gives oscillatory error

A better method is Gauss seidel

### [[Gauss-Seidel method]]
So here we use the new values that we found, when calculating the newer values.
So $\phi_{1,new}$ is used in calculating $\phi_{2,new}$ and so on.

Note that we can use relaxation on it aswell. $\omega$ is the relaxation factor
$\omega > 2$, will always lead to divergence. smaller $\omega$ will help to stabilize the solution
$\omega > 1$ is over relaxation. Gives faster convergence
$\omega < 1$, under relaxation. Gives more precise solution.

#### [[Convergence of GS method]]
If the value of the point on the diagonal is larger than the off diagonal elements the solution will converge. This is the sufficient condition for diagonal dominance.
If this criterion is not met the solution might diverge.


### More advanced method
So GS is just a simple method. There are more advanced, that are widely used for heavy CFD problems, as they converge faster.

#### [[Incomplete LU family]]
The normal LU decomposition solves the solution in one iteration. This is a very slow method
for large matrices. The incomplete LU family is an iterative method.
#### [[Conjugate Gradient family]]
Conjugate gradient method: Fast convergence, steps are take in conjugate (orthogonal w.r.t. A) directions. Goes in the direction of the largest gradient.
Notice that Conjugate Gradient is less sensitive to lack of diagonal dominance.
### Discussion on convergence
![[Pasted image 20220531115958.png]]

## Take homes:
![[Pasted image 20220531120028.png]]
