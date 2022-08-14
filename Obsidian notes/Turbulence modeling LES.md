# LES
So in LES we solve the filtered navier stokes FNS.
LES has 4 steps:

1) A Filterning operation is chosen
2) The Navier stokes is the filtered
3) A closure model is chosen
4) Numerical simulation of the FNS


So In LES, we model just some of the eddies. A rule of thumb is to get at least 80% of the turbulent kinetic energy covered.
![[Pasted image 20220527112731.png]]


We include the largest energy containing eddies, but model the dissipative effect of the smallest dissipative eddies.

Also there are different filters. it's best to just do the Fourier transform and have a hard cutoff. BUT this is not always possible, so sometimes we use a gauss filter. If we use a gauss filter we can always recover the unfiltered data. This is not possible with the Fourire method.


![[Pasted image 20220527112828.png]]
![[Pasted image 20220527112839.png]]

![[Pasted image 20220527112849.png]]
![[Pasted image 20220527112859.png]]

![[Pasted image 20220527112910.png]]![[Pasted image 20220527112916.png]]
![[Pasted image 20220527112936.png]]
![[Pasted image 20220527112954.png]]
![[Pasted image 20220527113012.png]]
![[Pasted image 20220527113023.png]]



![[Pasted image 20220527090703.png]]
smaller eddies have higher wavenumber.
