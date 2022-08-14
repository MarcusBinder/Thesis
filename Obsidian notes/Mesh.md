# Mesh generation
## Types of grids
When talking about grids, we have 2 main types.
**Structured** and **unstructured**

### Structured grids
This is: 
- H-grid
- O-grid, the grid can wrap around
- C-grid. here it wraps around, but dont collaps. Like over airfoil-
![[Pasted image 20220528114951.png]]

The lines cross each other one time
### Unstructured grids
Unstructured grids are the most widely used in the industry.
We can use different cells, do local refinements. All kind of fancy stuff, like wall layers and so on.
![[Pasted image 20220528115133.png]]


## Grid generation
It consist of:
1) Define the flow domain
2) Generate a surface grid
	1) It is important to have a high quality mesh on the surface!
3) Generate the volumetric grid

Note that if we use triangular mesh, we need to satisfy [[Delanuay condition]]
This states that no other vertices should be inside the circle.

## FVM generalized

![[Pasted image 20220528120428.png]]

Note that unstructured grids will be slower, as we now have more faces.

We want to project the point k' down to k to calculate $\phi_k$. Note that N is the neighbour point. This is called deferred correction. It is necessary if the grids are not orthogonal. This is what snGradSchemes/laplacianSchemes 
are used for in openFoam.
![[Pasted image 20220528121524.png]]

Also it is computational expensice to do the correction.


## High quality mesh
- Cell faces should be normal to the lines connecting the nodes as much as possible, (Cartesian grid: angle = 0 is perfect)
- Hexahedral grids are generally more accurate then triangular grids
- One set of grid lines should closely follow the streamlines as much as possible
- The grid should be fines where there are large gradients of velocity, pressure, temperature etc.
- Rapid variations in grid size is not good
- If too much of the flow does not go through the elements ortogonal it might lead to false diffusion
![[Pasted image 20220528121549.png]]

### Grid quality metrics

![[Pasted image 20220528122150.png]]
I ansys skewness is a combination of the above.

![[Pasted image 20220528122215.png]]
![[Pasted image 20220528122225.png]]