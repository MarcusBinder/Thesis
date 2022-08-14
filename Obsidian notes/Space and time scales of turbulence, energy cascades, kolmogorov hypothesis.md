# Space and time scales of turbulence

There is apparently this thing:

$$
Re \sim \dfrac{l_0}{\eta} \gg 1
$$
It says that there is a connection between the Reynolds number and the length scale of the largest motions (**$l_0$**) and the length scale at where the viscous dissipation kicks in (**$\eta$**). 
![[Pasted image 20220519152201.png]]


From the turbulent channel flow we had that:
$$
Re_\tau = \dfrac{\delta}{\delta_\nu}
$$
Where $\delta_\nu =\dfrac{\nu}{u_\tau}$

This means that if the reynolds number increases, then $\delta_\nu$ must increase. This is because that $\delta$ is constant as dictated by the dimensions.  Note that $\delta$ is half the channel width.

## Energy cascade
**Richardson energy cascade**

An eddy is a region of space with coherent vorticity. 
The energy is transferred from the larger eddies to the smaller ones through breakups.
The smallest eddies are stable and then dissipated. 

![[Pasted image 20220519155333.png]]


## Kolmogorov hypothesis
Also called **K41**, as it is from 1941.
Yields very fundamental results about turbulent flows.
The **K41** relies on 3 hypotheses:
- 1: Local isotropy
	- States that at sufficiently Reynolds number, the small-scale eddies are statistically isotropic
- 2: First similarity hypothesis
	- At sufficiently high Reynolds number, the statistics of the small-scale eddies have a universal form, that are uniquely determined by $\nu$ and $\epsilon$
	- He have these **Kolmogorov scales:**
	- Length (length of smallest eddies): $$ \eta = (\nu^3/\eta)^{1/4} $$ Velocity: $$ u_\eta = (\eta \nu)^{1/4} $$
	- Time (the time hat the smallest eddies are "alive"): $$ \tau_\eta =(\nu/\epsilon)^{1/2} $$
	- He also found:
	- $$
\begin{align*}
\eta/l_0 \sim Re^{-3/4} \\
u_\eta/u_0 \sim Re^{-1/4}  \\
\tau_\eta/\tau_{0} \sim Re^{-1/2} 
\end{align*}

$$
- 3: Second similarity hypothesis:
	- At sufficiently high Reynolds number, the statistics of the eddies of intermediate size have a universal form that is uniquely determined by $\epsilon$, but independent of $\nu$
	- This hypothesis are for the eddies in the inertial subrange (green). 
	- ![[Pasted image 20220519162026.png]]
	- ![[Pasted image 20220519162237.png]]




