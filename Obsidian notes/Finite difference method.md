# Finite difference method (FDM)
So we want to solve the generic transport equation
$$
\dfrac{\partial}{\partial t}(\rho \phi) + \dfrac{\partial}{\partial x_j}(\rho u_j \phi) = \dfrac{\partial}{\partial x_j} \left(\Gamma \dfrac{\partial \phi}{\partial x_j} \right) + q_\phi
$$
Here $\phi$ is the unknown value, and $\rho, v, \Gamma$ and $q_\phi$ are the known values.

We solve the equation on discrete points (nodes) in space. So we need a numerical grid. Note that we normally only use FDM on structured grids.
![[Pasted image 20220528103920.png]]

## Approximation of derivatives
So we have some differential equation, now we need to *discretize* it. 

### Approximation of first derivative
The slides can be seen here:
[[Approximation of first derivative]]

But in conclusion, we use a [[taylor series]] to approximate the first derivatives. 
We can then "cut" off the higher order terms that we dont want, and call that bitch for a truncation error.

When we do the appriximation, we can either use the points infront of where we are (**FDS**), we can use the points behind (**BDS**) or we can use the point in front and behind (**CDS**)
![[Pasted image 20220528110254.png]]
Also to increase the order you can increase the number of points in you approximation.

### Approximation of second derivative
Slides here:
[[Approximation of second derivative]]

So if we want to do the approximation for the second order derivative, there are 3 approaches.

1) is to differentiate the first derivative
   ![[Pasted image 20220528113238.png]]
2) Use Taylor series
   ![[Pasted image 20220528113318.png]]
3) Fit a polynomial, and take the 2nd derivative
   ![[Pasted image 20220528113415.png]]

### Cost of approximations
The higher order, the more operations and the more computational expensive
Also if we have more nodes, then the treatment of the buandary becomes more difficult.

Very high order approximations are only justified for DNS or for turbulent flows.
**For most practical problems, 2nd order approximation is the best tradeoff**


## Solving FDM




## Method
We discretize the geometry, to get discrete points that can be described with differential equations.
We need to calculate the derivatives using discrete points.

Notes on FDM:
- When different terms are approximated with different schemes, the overall error is controlled by the lowest order
- CDS can lead to non-physical oscillations when capturing sharp gradients. 
- The upwind schemes (BDS/FDS) does not lead to oscilations, but adds more diffusion to the solution $$
  \dfrac{\partial}{\partial x} (\rho u \phi) = \left( \Gamma \dfrac{\rho u \Delta x}{2}  \right) \dfrac{\partial^2 \phi}{\partial x^2}
  $$
  Where $\rho u \Delta x/2$ is the artificial/false diffusion coefficient.
  