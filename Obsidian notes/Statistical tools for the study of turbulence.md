## Statistical tools for the study of turbulence
So as turbulence is quite random, we make use of statistics to help us out. 
Here are some terms that we need to know:
**PDF** is the probability density function
A function is completely characterized by its PDF p(v)

Some properties of the PFD are:
- $p(v) \geq 0$ for v between minus infinity and infinity
- $p$ is normalized so that $\int_{-\infty}^{\infty}p(v) dv =1$ 
- $p(-\infty)=p(\infty)=0$ as no physical variables reach an infinite value
- the probability P of u to have a magnitude in $[v_1,v_2]$ is $P(v_1<u_i<v_2)=\int_{v1}^{v2}p(v)dv$

The **mean** of a random variable u is:
$$\langle u \rangle = \dfrac{1}{N} \sum_{i=1}^N u_i$$

This is just the normal mean that we know. It is a linear operator, that means:
$$ \langle F(u)+G(u) \rangle = \langle F(u) \rangle + \langle G(u) \rangle
$$
Also note that: $\langle \langle u\rangle \rangle = \langle u \rangle$

We then define the fluctuation as:
$$u' = u-\langle u \rangle 
$$
The variance is then:
$$ var(u) = \langle u'^2 \rangle = \dfrac{1}{N} \sum _{i=1}^N u_i'^2
$$
The standard deviation is the root mean square of u:
$$ sdev(u) = \sqrt{var(u)} = \langle u'^2\rangle^{1/2}
$$
We also have the n'th central moment as:
$$
\mu_n = \langle u'^n \rangle = \dfrac{1}{N} \sum_{i=1} ^N (u_i - \langle u \rangle)^n 
$$
The final terms to know is the skewness and flatness:
Skewness:
$$S = \dfrac{\langle u'^3 \rangle}{\sigma^3} = \dfrac{\dfrac{1}{N}\sum_{i=1}^N u_i'^3}{\sigma^3}
$$
Flatness:
$$
\delta = \dfrac{\langle u'^4 \rangle}{\sigma^4} = \dfrac{\dfrac{1}{N}\sum_{i=1}^N u_i'^4}{\sigma^4}
$$
Where $\sigma$ is the standard deviation of u.
![[Pasted image 20220517093158.png]]

### Averaging
There are 2 types of averages we do:
**Time averaging**

![[Pasted image 20220517095200.png]]
**Ensemble averaging**

![[Pasted image 20220517095235.png]]

Time averaging is just the normal mean that we all know and love, but ensemble averaging is when we do the same experiment multiple times and then average them over.

**Time averaging** can only be used when the mean velocity is steady (constant position in the
wind tunnel).
**Ensemble averaging**: Reservoir empty (open tap) Measurement as a function of time.
**Space averaging:** Used with numerical simulation data.
We also have space averaging, but I dont think this is used lol. It's for simulated data apparently.
![[Pasted image 20220517095425.png]]
Where m is the number of members in the space.

### Stationarity, homogeneity and isotropy
This is the last stuff about statistics.

**Stationarity**
$$ \langle u(x_1,t_1) u(x_2,t_2)...u(x_n,t_n)\rangle = \langle u(x_1,t_1+\tau) u(x_2,t_2+\tau)...u(x_n,t_n+\tau) \rangle
$$
This means that the statistics doenst change over time. Steady flow.

**Homogeneity**
$$
\langle u(x_1,t_1) u(x_2,t_2)...u(x_n,t_n) \rangle = \langle u(x_1+y,t_1 u(x_2+y,t_2)...u(x_n+y,t_n) \rangle
$$

The statistic doesnt change with space. The statistic is the same no matter where we measure. 

**Isotropy**
The statisticals are independent of the direction of space. That means that we can rotate the coordinate system and the measurements are the same.
Isotropy means that:
![[Pasted image 20220517113444.png]]
