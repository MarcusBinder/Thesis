# DNS
So DNS means that all the scales of motion are resolved. That means that:
![[Pasted image 20220529120106.png]]
The modeling errors are zero, and the discretization, iteration and round-off are almost zero as we have a fine mesh/higher order.

### Advantage of DNS
Gives the full 3D instantaneous flow field
Any desired quantity can be measured at any location
Analysis are only limited by the mind of the researcher (and computational power)

Note that DNS can still give wrong results, from simplifies equations (constant properties) or BC's (inaccurate inflow conditions... so on)

![[Pasted image 20220529120459.png]]

## Cost of DNS
A lot!

The 3D grid size is:
$$
N_x N_y N_z \sim Re^{9/4}
$$
The spatiotemporal grid size is:
$$
N_x N_y N_z N_t \sim Re^{11/4}
$$

## Speed up 
It can also be sped up, using parallel computing.
![[Pasted image 20220529121031.png]]
![[Pasted image 20220529121037.png]]

