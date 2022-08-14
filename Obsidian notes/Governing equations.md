# Governing equations
So to do this CFD stuff, we are going to use some equations.
These are the **conservatory equations** 
They will be listed below:

## Mass Conservation
As the mass inside the control volume cannot just disappear or appear, the following must hold true:
$$
\dfrac{\partial}{\partial t} \int_V \rho dV+ \int_S \rho \textbf{v} \cdot \textbf{n} dS=0 \hspace{3 cm} \text{Integral form}
$$
$\dfrac{\partial}{\partial t} \int_V \rho dV$ This is the rate of change of mass inside the volume. This is calculates by taking the integral over the whole volume
$\int_S \rho \textbf{v} \cdot \textbf{n} DS$ This is the mass flux into/out of the boundary. This is calculated by a surface integral.

If we use [[Gauss divergence theorem]] to the convection term, it is possible to transform the surface integral into a volume integral. The control volume can then be shrunk down to be infinitesimal small and we can write the equation in the differential form:
$$
\dfrac{\partial \rho}{\partial t} + \nabla \cdot (\rho \textbf{v})=0 \hspace{3 cm} \text{Differential form}
$$
![[Pasted image 20220131140103.png]]

The differential form can be written with index notation as:

$$
\dfrac{\partial \rho}{\partial t} + \dfrac{\partial (\rho \textbf{u}_i)}{\partial \textbf{x}_i} = \dfrac{\partial \rho}{\partial t} + 
\dfrac{\partial (\rho \textbf{u}_x)}{\partial \textbf{x}_x} +
\dfrac{\partial (\rho \textbf{u}_y)}{\partial \textbf{x}_y} +
\dfrac{\partial (\rho \textbf{u}_z)}{\partial \textbf{x}_z}
$$



## Momentum conservation
This is just Newtons 2. law. (change in momentum = sum of external forces)
![[Pasted image 20220131140630.png|ctr]]
It goes like this:
$$
\dfrac{\partial}{\partial t} \int_V \rho \textbf{V} dV + \int_S \rho \textbf{V}\textbf{V}\cdot\textbf{n}  dS= \int_S \bar{T} \cdot\textbf{n} dS+ \int_V \rho \textbf{g} dV \hspace{3 cm} \text{Integral form}
$$
This can be written in differential form using [[Gauss divergence theorem]] as well, to give:
$$
\dfrac{\partial}{\partial t}  \rho \textbf{V} + \nabla ( \rho \textbf{V}\textbf{V})= \nabla \bar{\bar{T}} + \rho \textbf{g}  \hspace{3 cm} \text{Differential form}
$$


The last term: $\int_V \rho \textbf{g} dV$ is simply the volumetric forces

This term: $\int_S \bar{\bar{T}} \cdot\textbf{n} dS$  is the surface forces. We have that $\bar{T}$ is the stress tensor. This is expressed as:
$$
\bar{\bar{T}} = - \left(p + \dfrac{2}{3} \mu \nabla \cdot \textbf{V} \right) \textbf{I} + 2 \mu D
$$
Where
$$
D = \dfrac{1}{2} [\nabla \textbf{V} + (\nabla \textbf{V})^T ]
$$
Note that this is only the stress tensor for [[Newtonian fluids]]. If we have non newtonian fluids then we would use another formula.
In the equation we have the following:

Symbol | Description
-------|-----------
$\mu$      |    Dynamic viscosity
I  |  Is the identity tensor
p      | Is the static pressure
D       | Is the rate f strain (deformation) tensor


In Tensor notation, this becomes:
$$
T_{ij} = - \left( p + \dfrac{2}{3}\mu \dfrac{\partial u_j}{\partial x_j} \right) \delta_{ij} + 2 \mu D_{ij}
 $$
With 
$$
D_{ij} = \dfrac{1}{2} \left( \dfrac{u_i}{x_j} +\dfrac{u_j}{x_i}  \right)
$$

Also it might be important to remember this:
$$
\dfrac{\partial u_j}{\partial x_j}= \dfrac{\partial u_1}{\partial x_1} + \dfrac{\partial u_2}{\partial x_2}+\dfrac{\partial u_3}{\partial x_3} =  \nabla u
$$
That means that if we have **incompressible flow**, the last term in the brackets for the $T_{ij}$ drops out


## Energy conservation

(Change in energy content = heat transfer + work)
From the second (?) law of thermodynamics we have that energy must be conserved!

![[Pasted image 20220201133652.png]]

The formula is:
$$
\dfrac{\partial}{\partial t} \int_V \rho h dV + \int_S \rho h \textbf{V} \cdot \textbf{n} dS= - \int_S \textbf{q} \cdot\textbf{n} dS + \int_V \text{(viscous heating + compression work) } dV \hspace{1 cm} \text{Integral form}
$$


Again by using [[Gauss divergence theorem]] we can get the differential from as:
$$
\dfrac{\partial}{\partial t} \rho h + \nabla (\rho h \textbf{V}) = - \nabla \textbf{q}  + \text{(viscous heating + compression work) }  \hspace{1 cm} \text{Differential form}
$$
In many cases the viscous heating and compression work can be neglected!

$\dfrac{\partial}{\partial t} \int_V \rho h dV$ This is the change in the internal energy in the control volume
$\int_S \rho h \textbf{V} \cdot \textbf{n} dS$ This is the energy flow inside or out of the control volume

We can also write the following approximations/formulations:
$$\textbf{q} = -k \nabla T \hspace{1 cm} \text{Fourier's Law}  $$
$$
dh \approx c_p dT
$$
This gives the energy equation in terms of temperature:
$$
\dfrac{\partial}{\partial t} (\rho c_p T) + \nabla (\rho \textbf{V} c_p T) = - \nabla (k \nabla T) 
$$
## Simplifications
So there are some simplifications we can use.
If the temperature gradient is small, then we can use constant values for k (Thermal conductivity) and $\mu$ (Dynamic viscosity).

Also we can assume the flow to be incompressible when:
$$
M< 0.3
$$
For detail see this: [[Simplification Mach number]]

## incompressible vs compressible solution
If we have **compressible flow** our equations are as follows:

Mass:
$$
\dfrac{\partial \rho}{\partial t} + \nabla \cdot (\rho \textbf{v})=0 \hspace{3 cm} \text{1 scalar equation}
$$
Momentum:
$$
\dfrac{\partial}{\partial t}  \rho \textbf{V} + \nabla ( \rho \textbf{V}\textbf{V})= -\nabla p + \nabla \bar{\bar{\tau}}  \hspace{3 cm} \text{Vector (3 scalar equations)}
$$
Energy:
$$
\dfrac{\partial}{\partial t} \rho c_p T + \nabla (\rho c_p \textbf{V} T) = \nabla (k \nabla T)   \hspace{1 cm} \text{1 scalar equation}
$$

But this only gives 5 equation, and we have 6 unknowns:
- $\rho$ density
- v velocity in x, y and z
- T temperature
- p pressure

The following are regarded as known function of temperature and pressure:
- $c_p$
- k
- $\mu$
That means we have to use the equation of state as well.
This is  just from the ideal gas law, so we can describe the pressure as a function of temperature and density.

Each equation has one dominant variable, so they are easy to solve...
BUT if we have a low Mach number, then the equation becomes [[stiff equation| stiff]], so it might be best to solve it as if it was incompressible.

If we have **incompressible flow** our equations are as follows:

Mass:
$$
\nabla \cdot \textbf{v}=0 \hspace{3 cm} \text{1 scalar equation}
$$
Momentum:
$$
\dfrac{\partial}{\partial t}  \rho \textbf{V} + \nabla ( \rho \textbf{V}\textbf{V})= -\nabla p + \nabla \bar{\bar{\tau}}  \hspace{3 cm} \text{Vector (3 scalar equations)}
$$
Energy:
$$
\dfrac{\partial}{\partial t} \rho c_p T + \nabla (\rho c_p \textbf{V} T) = \nabla (k \nabla T)   \hspace{1 cm} \text{1 scalar equation}
$$
Now our unknowns are:
- v velocity in x, y and z
- T temperature
- p pressure

Now the following are regarded as known function of temperature and pressure:
- $c_p$
- k
- $\mu$
- $\rho$ 

As the density and pressure are now decoupled, we dont need the EoS!

We dont have to solve the energy equation, but we can do so if we want to know the temperatures aswell.

Note that the pressure only appears in gradient from. That means that the absolute value of pressure is meaningless.


