# DNS modelling
So DNS is the big boy of modelling. You need to resolve all the eddies, which means a LOT of computational power!

![[Pasted image 20220521110613.png]]

As we need to resolve all the eddies, we must have some pretty small scales. These can be found approximately with the [[Kolmogorov scale]]. 
Also, we are solving the [[Navier-Stokes equation]], but it's non local. That means that we need to model the total domain, as one part can influence the other in a BIG way...

The smallest scale can be found from [[Space and time scales of turbulence, energy cascades, kolmogorov hypothesis#Kolmogorov hypothesis|Kolmogorov hypothesis]], where he found that the smallest length scale to be:

$$
\eta/l_0 \sim Re^{-3/4} \rightarrow \eta = \dfrac{l_0}{Re^{3/4}}
$$
The timescale is:

$$
\tau_\eta/\tau_{0} \sim Re^{-1/2} \rightarrow \tau_\eta = \dfrac{\tau_0}{Re^{1/2}}
$$
So we need to do much calculations, if the reynoldsnumber is somewhat large.

The whole point about this DNS stuff is that it is precise, but not really feasible.
It simply takes to much computational power if we want to simulate anything larger then small/simple stuff.

![[Pasted image 20220521113607.png]]