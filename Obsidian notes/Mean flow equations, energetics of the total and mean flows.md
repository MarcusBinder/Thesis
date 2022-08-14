# Mean flow equations
As turbulence is unsteady, it is hard to talk about specific values. BUT we are mostly interested in the statistical stuff like mean velocity, turbulence intensity, mean drag..... 


So mr [[Reynold]] camu up with whats called *Reynold decomposistion*
It's that some value can be found as the mean + the fluctuations.

$$u(x,t)= \langle u \rangle (x,t) + u'(x,t)
$$
From [[incompressibility condition]]
$$ \nabla u = 0
$$
If we write that out with the reynold decomposistion, we would get that
$$ \nabla \langle u \rangle = 0
$$
$$ \nabla u'= 0
$$
$$ \partial_j \langle u_j \rangle = 0
$$
$$ \partial_j u_j'  = 0
$$
These are all zero.
This makes use of the fact that the mean of the fluctuating part is zero $\langle u' \rangle =0$

## Reynolds equation for the mean flow
We can then take the mean of the [[Navier-Stokes equation]], to get:
$$
\partial_t \langle u_i \rangle + \langle u_j \rangle \partial_j \langle u_i \rangle = - \dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \langle u_i' u_j' \rangle 
$$
For [[Derivation of the mean Navier-Stokes]] check the link

Each term represents the following:
- I: Is the storage of momentum (inertia)
- II: IS the advection of mean momentum by the mean flow ??
- III: Mean pressure gradient forces
- IV: Influence of viscous stresses on the mean flow
- V: Influence of Reynold stresses on mean flow

We do all this because we want to look at the mean flow. BUT the Reynold stresses introduce 6 more unknowns to the problem. SO we have 10 unknowns now, and still only 4 equations. 3 from the continuity and 1 from conservation of mass.

### Reynolds stresses
We define this term:
$$\Sigma_{ij} = \langle u_i' u_j'\rangle
$$
This is the known as the **Reynolds stress tensor**. It is the velocity fluctuation covariances???.

We can rewrite the mean Naiver-stokes equation as:

$$
\partial_t \langle u_i \rangle + \langle u_j \rangle \partial_j \langle u_i \rangle =  \dfrac{1}{\rho} \partial_j \left(  -\langle p \rangle \delta_{ij} + \mu ( \partial_j \langle u_i \rangle + \partial_i \langle u_j \rangle)  - \rho \langle u_i' u_j' \rangle \right)
$$

We still have the closure problem... Meaning we cannot solve the reynold equation, as we have these reynold stresses. 
$\Sigma_{ij}$ is a second order tensor. It's symmetric and the diagonal elements $\Sigma_{ii} = \langle u_i'u_i'\rangle \geq 0$ are the normal stresses.
The off diagonals are the shear stresses?.

Notice that the term $\rho \langle u_i' u_j' \rangle$ is the apparent stess. This is because it's not really a stress, but it looks like the viscous stress... It's how the fluctuating field affect our mean field.

![[Pasted image 20220518100054.png]]

### kinetic energies
We are also going to define the following:
**Turbulent kinetic energy (TKE)**
$$k = \dfrac{1}{2} \langle u_i' u_i' \rangle = \dfrac{1}{2}(\langle u_i'^2 \rangle +\langle v_i'^2 \rangle+\langle w_i'^2 \rangle ) 
$$
This is the half of the diagonal of the stress tensor. 

**Kinetic energy of mean flow (KEM)**
$$
\bar{K} = \dfrac{1}{2} \langle u \rangle \langle u \rangle 
$$
**Mean kinetic energy (MKE)**
$$
\langle K \rangle = \langle u u \rangle = \bar{K} + k
$$
## Governing equation for TKE
So now we want to find a governing equation for the TKE $k = \dfrac{1}{2} \langle u_i' u_i' \rangle$

We are going to do this by subtracting the **Reynold equation** from the **Navier stokes**. Here we removes everything that is not fluctuating

**NS**: 
$$
\partial_t u_i + u_j\partial_j u_i = -\dfrac{1}{\rho} \partial_ip+\nu \partial_j \partial_ju_i
$$
**RE**:
$$
\partial_t \langle u_i \rangle + \langle u_j \rangle \partial_j \langle u_i \rangle = - \dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \langle u_i' u_j' \rangle 
$$
**NS-RE**:
$$
\partial_t  u_i'  + \langle u_j \rangle \partial_j  u_i'  = - \dfrac{1}{\rho} \partial_i  p'  + \nu \partial_j \partial_j  u_i'  - \partial_j \Pi_{ij} 
$$
Where $\Pi_{ij} = u_j' \langle u_i \rangle + u_i' u_j' - \langle u_i' u_j' \rangle$

BUT we note that k is a scalar equation and the NS-RE is a vector equation. So we multiply it with $u_i'$. The equation then becomes:
$$
\big\langle u_i' \times \left(\partial_t  u_i'  + \langle u_j \rangle \partial_j  u_i'  = - \dfrac{1}{\rho} \partial_i  p'  + \nu \partial_j \partial_j  u_i'  - \partial_j \Pi_{ij} \right)  \big\rangle
$$
If we multiply it all inside, we end up with:

$$
\partial_t k + \langle u_j \rangle \partial_j k + \partial_j T'_j = \mathcal{P} - \epsilon 
$$

Where:
$\mathcal{P} = -\langle u_i' u_j' \rangle \partial_j \langle u_i \rangle$  this is the production of TKE
$\epsilon = 2\nu \langle s_{ij}' s_{ij}' \rangle$ this is the rate of viscous dissipation of the turbulent flow.
	$s_{ij}' = \dfrac{1}{2} (\partial_i u_j' + \partial_j u_i')$
$T_j' = \dfrac{\langle u_j' p'}{\rho} - 2 \nu \langle s_{ij}' u_i' \rangle + \dfrac{1}{2} \langle u_j'u_i'u_i' \rangle$ This is the turbulent flux energy.

![[Pasted image 20220518114341.png]]


WE STILL HAVE THAT GOSH DARN CLOSUREPROBLEM!