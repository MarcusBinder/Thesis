# RANS modelling

RANS modelling is modelling the [[Navier-Stokes equation#Reynold averaged Navier stokes | Reynold averaged Navier Stokes]] equation.

$$
D_t \langle u_i \rangle =\partial_t \langle u_i \rangle + \langle u_j \rangle \partial_j \langle u_i \rangle = - \dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \langle u_i' u_j' \rangle 
$$
$$
\partial_i \langle u_i \rangle = 0
$$

BUT we have some problems as we have 4 equations (3 momentum equations and 1 continuity), but 10 unknowns:
$\langle u_i \rangle$    = 3 unknowns
$\langle p \rangle$      = 1 unknown
$\langle u_i'u_j' \rangle$ = 6 unknowns (actually a 3x3 tensor, but it's symmetric at the diagonal, so only 6 unknowns.)

This means that we have a **closure problem**.
So to close the Reynolds equations we say that:
$$
\Sigma_{ij} = \langle u_i'u_j' \rangle = \mathcal{F}(\langle u_i\rangle, \text{other mean quantities})
$$
So we say that the reynolds stresses are a function of the mean flow, AND some other stuff.
There are the following different approaches:
- **Zero equation models**
	- This is just solving algebraic models of constant eddy-viscosity **and** mixing length
	- They are divided into 2 groups...
- **One equation models**
	- Turbulent kinetic-energy models
- **Two equation models**
	- $k-\epsilon$ and $k-\omega$ models.
- **Full Reynold stress models**
	- Solves 6 equations. SSG and LRR models.


## Eddy viscosity models
So we need to model the Reynolds stresses $\langle u_i' u_j' \rangle$
We do a lot of stuff. The fluid mechanics 101 guy uses the Brownian motion argument, but i'm pretty sure that Mahdi used some sort of similarity argument. He said that we have A that looks like this, so B must be somewhat similar...
But fuck it, lets just get to the result...
### Eddy-viscosity hypothesis
I think this is also the Boussinesq hypothesis.
But we end up with:
$$
\Sigma_{ij} = \langle u_i'u_j' \rangle = \dfrac{2}{3}k \delta_{ij} - \nu_T (\partial_j \langle u_i \rangle+ \partial_i \langle u_j\rangle)
$$
We also use this form:
$$
\langle u_i'u_j' \rangle = \dfrac{2}{3}k \delta_{ij} - 2\nu_T \bar{S}_{ij}
$$
where $\bar{S}_{ij} =(1/2)(\partial_j \langle u_i \rangle+ \partial_i \langle u_j\rangle)$ and is called the **mean rate of strain**


BUT we still need to model $\nu_T$ and maybe the $k$ also...

Note that $\nu_T$ has the dimmensions of: $[\dfrac{m^2}{s}= \dfrac{m}{s} \cdot m]$, it's velocity times length.
This means we model it as a velocity multiplied with a distance.

$$
\nu_T = u_T \cdot l_t
$$

### Zero equation models
There are 2 approaches here.

**Approach 1**
This is just taking it to be a constant
$\nu_T = Cst$
This is a shit model.

**Approach 2**
This is called the **mixing length model**
We argue that the size of the eddy is proportional to the distance.
Here we have that:
$$
l_t = l_m
$$
The length is specifies in terms of the geometry of the flow.

$$
u_T = l_m (2\bar{S}_{ij}{S}_{ij})^{1/2}
$$
This means that:
$$
\nu_T = l_m^2 (2\bar{S}_{ij}{S}_{ij})^{1/2} = l_m^2 |\dfrac{d\langle u\rangle}{dy}|
$$
We use that $l_m = ky$ in the log-law region. k=0.4 approximately.

### One equation models
This is an improvement of the mixing length model.
We calculate the $u_T$ now as a value from the turbulent kinetic energy.
$$
u_T = c \cdot \sqrt k
$$
c is just a constant $c \approx 0.55$, from experiments.
We must still specify the $l_m(x,t)$, and the turbulent kinetic energy can be calculated or estimated. We need to solve one model transport equation for k.

**Methodology**
Here is a step by step guide to use a **one-equation model**
Also remember that:
$$
\Sigma_{ij} =  \langle u_i' u_j' \rangle = \dfrac{2}{3}k \delta_{ij}- \nu_T (\partial_j \langle u_i \rangle + \partial_i \langle u_j \rangle)
$$
1) Specify the mixing length $l_m(x,t)$
2) Solve a model transport equation for $k(x,t)$
3) Compute the turbulent viscosity$$
		\nu_t(x,t) = c \sqrt{k(x,t)}\cdot l_m(x,t)$$
4) Compute the Reynolds stresses $\Sigma_{ij}$
   $$ \Sigma_{ij} = \langle u_i' u_j' \rangle = \dfrac{2}{3}k(x,t)\delta_{ij}-c\sqrt{k(x,t)}l_m(x,t) (\partial_j \langle u_i \rangle + \partial_i \langle u_j \rangle)
   $$
5) solve the **modeled** Reynolds equation for the mean flow:
   $$\partial_t \langle u_i \rangle+ \partial_j (\langle u_i \rangle \langle u_j \rangle) = - \dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \left( \dfrac{2}{3}k \delta_{ij}-c\sqrt{k}l_m (\partial_j \langle u_i \rangle + \partial_i \langle u_j \rangle) \right)
   $$$$\partial_i \langle u_i \rangle =0
   $$
This requires the specification of $l_m(x,t)$ and a model transport equation for $k(x,t)$
Gives you: $\langle u \rangle$, $\langle p \rangle$, $l_m$, and k. (indirectly $\nu_T$ and $\langle u_i' u_j' \rangle$)

**The Transport equation for $k(x,t)$  **

$$
\partial_t k + \langle u \rangle \cdot \nabla k + \nabla \cdot T' = \mathcal{P}-\epsilon
$$
Here we have that 
$$
T_i' = \dfrac{1}{2}\langle u_j' u_j' u_i' \rangle + \dfrac{\langle u_i' p' \rangle}{\rho} - 2 \nu \langle s_{ij}' u_j' \rangle
$$
$$
\mathcal{P} = - \langle u_i' u_j' \rangle \partial_j \langle u_i \rangle
$$
$$
\epsilon = 2 \nu \langle s_{ij}' s_{ij}' \rangle
$$
We have the problem that $\epsilon$ and $\nabla T'$ is not in closed form!
**What to do about** $\epsilon$
So from the [[Space and time scales of turbulence, energy cascades, kolmogorov hypothesis#Kolmogorov hypothesis|Kolmogorov's second similarity hypothesis]],  we know that the dissipation of the smallest scales, scales with the energy transfer of the larges scales:

$$
\epsilon \propto \dfrac{u_0^3}{l_0} \rightarrow \epsilon = C_D \dfrac{k^{3/2}}{l_m}
$$
This is probably found from dimensional analysis. $C_D$ is a model constant. 
Note that in reality, it is  not really a constant, but I guess it's close enough.
![[Pasted image 20220526144637.png]]

**What to do about** $T_i'$
Here we simply use the *gradient-diffusion hypothesis:*
$$
T' = - \dfrac{\nu_T}{\sigma_k}\nabla k
$$
Here we have that $\sigma_k$ is the "turbulent Prandtl number". Apparently often just set to $\sigma_k = 1$
This hypothesis is simple and easy to implement.

It all gives this transport equation:
$$
\bar{D}_t k = \nabla \cdot \left(  \dfrac{\nu_T}{\sigma_k} \nabla k \right) + \mathcal{P} - \epsilon
$$
BUT the drawback is that it's incomplete as we still need mixing length.

### Two equation models 

#### $k-\epsilon$ model
This is still a turbulent-viscosity modeling approach.
From dimensional analysis we can see that:
$$
\nu_T \propto \dfrac{k^2}{\epsilon}
$$
So now we dont need no stupid mixing length!
This is one of the most widely used models in CFD...


**Methodology for k -$\epsilon$**
Here is a step by step guide to use the model


1) Solve a model transport equation for $k(x,t)$
   $$
\bar{D}_t k = \nabla \cdot \left(  \dfrac{\nu_T}{\sigma_k} \nabla k \right) + \mathcal{P} - \epsilon
$$
2) Solve a model transport equation for $\epsilon$  
3) Compute the turbulent viscosity$$
		\nu_t(x,t) = C_\mu \dfrac{k^2}{\epsilon}$$
		Note that $C_\mu$ is one of **5 constant**, in this model
4) Compute the Reynolds stresses $\Sigma_{ij}$
   $$ \Sigma_{ij} = \langle u_i' u_j' \rangle = \dfrac{2}{3}k(x,t)\delta_{ij}-C_\mu \dfrac{k^2}{\epsilon}(\partial_j \langle u_i \rangle + \partial_i \langle u_j \rangle)
   $$
5) solve the **modeled** Reynolds equation for the mean flow:
   $$\partial_t \langle u_i \rangle+ \partial_j (\langle u_i \rangle \langle u_j \rangle) = - \dfrac{1}{\rho} \partial_i \langle p \rangle + \nu \partial_j \partial_j \langle u_i \rangle - \partial_j \left( \dfrac{2}{3}k(x,t)\delta_{ij}-C_\mu \dfrac{k^2}{\epsilon}(\partial_j \langle u_i \rangle + \partial_i \langle u_j \rangle) \right)
   $$$$\partial_i \langle u_i \rangle =0
   $$
$\epsilon$ is viewed as the energy-flow rate down the cascade. 
The standard k-epsilon modes use an empirical equation for the transport of epsilon.
$$
\bar{D}_t  \epsilon = \nabla \left( \dfrac{\nu_T}{\sigma_\epsilon} \nabla \epsilon  \right) + C_{\epsilon1} \dfrac{\mathcal{P}\epsilon}{k}-C_{\epsilon2} \dfrac{\epsilon^2}{k}  
$$
The constants for the standard model is: $C_\mu = 0.09, C_{\epsilon1} = 1.44,  C_{\epsilon1} = 1.92, \sigma_k = 1, \sigma_\epsilon = 1.3$

We can easily see that it looks a lot like the transport equation for k:
   $$
\bar{D}_t k = \nabla \cdot \left(  \dfrac{\nu_T}{\sigma_k} \nabla k \right) + \mathcal{P} - \epsilon
$$
Note that the models do allright for simple flows, but are inaccurate for complex flows.
Also we need some of that wall treatment.

#### $k-\omega$ model
Now we have $\omega$, this is the turbulence frequency: $\omega = \dfrac{\epsilon}{k}$

We then have the transport equation for omega as:
$$
\bar{D}_t  \omega = \nabla \left[ \left( \nu + \dfrac{\nu_T}{\sigma_\omega} \right) \nabla \omega  \right] + C_{\omega1} \dfrac{\mathcal{P}\omega}{k}-C_{\omega2} \dfrac{\omega^2}{k}  
$$
It is seen as a more general model then k-epsilon. 

### Shortcomings of eddy-viscosity models
![[Pasted image 20220526160558.png]]

#### Full six-equation reynolds stress models.
There is only this slide...
![[Pasted image 20220526160654.png]]
