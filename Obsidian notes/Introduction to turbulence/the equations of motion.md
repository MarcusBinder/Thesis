
## Introduction to turbulence/the equations of motion
Our good friend mr. [[Reynold]] came up with this number (not really him, but named after him):
$$
Re = \dfrac{U\cdot L}{\nu} = \dfrac{U \cdot L \cdot \rho}{\mu} \approx \dfrac{\text{Inertial forces}}{\text{Viscous forces}}
$$
As we have that: $\nu =\dfrac{\mu}{\rho}$
Here we have that:
$$
U [m/s] = \text{Velocity scale, it's the average velocity} 
$$
$$
L [m] = \text{Length scale, it's the scale of the larges eddies} 
$$
$$
\nu [m^2/s] = \text{Kinematic viscosity} 
$$
So they found that at approximately 2300 we get turbulent flow.

![[Pasted image 20220516094951.png]]
So as the Reynolds number increases, the flow becomes "more" turbulent.

### Properties of turbulence
So Turbulence is apparently hard to define, but we have that:
- Turbulent flows are highly unsteady
- Three dimensional
- Random-like (SIKE not really)
- Turbulence increses mixing and transport rates (the fluxes)
- It can be visualized as consisting of irregular swirls of motion called eddies
- Continuous spectrum of eddy sizes - ranging from the integral scale to the [[Kolmogorov scale]] (viscous dissipation)

It is really hard to define turbulence. It's a [[chaotic system]]
It's governing equation is known([[Navier-Stokes equation]]), but we dont have any analytical solution in turbulent flows.

A big aspect of turbulence is the **Energy cascade**
![[Pasted image 20220516101526.png]]
Here we have that the big eddies of size L breaks down into smaller eddies. This is called the energy cascade. They don't lose any energy, only size.
Then at some point the eddies becomes so small that they reach the [[Kolmogorov scale]] and dissipate their energy to the viscous effects.

There is this relation between the largest and smalles eddies:
$$\dfrac{L}{\eta} \approx Re^{3/4}

$$
That means that the larger Reynolds number, the bigger difference between the larges and smallest eddies.

## Governing equations
Note that we only have:
- Newtonian fluids
- Incompressible flows
- Constant and uniform properties. Density and mu constant.

### Conservation og mass and incompressibility condition
So we have these 2 conditions.
Conservation of mass is given by the continuity equation:
$$\partial_t \rho+ \partial_j(\rho u_j) = 0
$$
And as we have constant density, *[[incompressibility condition]]*
$$\partial_j u_j = \nabla u = 0
$$
This is called divergence free condition. Or that the velocity field in solenoidal. Aka no source or sink.

We now arrive at the [[Navier-Stokes equation]]. This is the conservation of momentum for a fluid particle:
$$
\partial_t u_i + u_j\partial_j u_i = -\dfrac{1}{\rho} \partial_ip+\nu \partial_j \partial_ju_i
$$
Note that we want to write it in conservative form (I think it's because this leads to smaller errors when solved by [[CFD]])
$$
D_t u_i =\partial_t u_i + \partial_j ( u_i u_j) = -\dfrac{1}{\rho} \partial_ip+\nu \partial_j \partial_ju_i
$$
Note that the following is applicable (using the chain rule of differentiation):
$$
\partial_j ( u_i u_j) = (\partial_j u_i) u_j + (\partial_j u_j) u_i 
$$
But as we have that $(\partial_j u_j)=0$ because of the incompressibility condition, we have the same as the equation above.

So we have this for the [[Navier-Stokes equation]]:
$$
\partial_t u_i + \partial_j ( u_i u_j) = -\dfrac{1}{\rho} \partial_ip+\nu \partial_j \partial_ju_i
$$
Where:
$\partial_t u_i$        is the storage of momentum (inertia)
$\partial_j ( u_i u_j)$  is the advection
$-\dfrac{1}{\rho} \partial_ip$   is the pressure gradient forces
$\nu \partial_j \partial_ju_i$   is the influence of viscous stresses

Can also be expressed as:
![[Pasted image 20220516112333.png]]

### Passive scalars
This is where the dynamics of this scalar has no effect on the fluid flow (one way coupling)
Example we can calculate the temperature of the flow, but this doesnt go the other way back.





