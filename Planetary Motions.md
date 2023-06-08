
The gravitational force on a planet with mass m can be described by the equation

![lagrida_latex_editor (2)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/c18c75d0-a469-4a8e-a658-940252e7394a)

where G is the gravitational constant, M is the mass of the central object (the Sun in our case), ![lagrida_latex_editor (3)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/8cb0c954-d5b7-489e-9b26-db3f8252210f) is the position vector from the planet to the Sun, r is the magnitude of the position vector, and ![lagrida_latex_editor (4)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/ca9ef961-3b7f-4e82-868d-269531d21e34) is the gravitational force vector.

By Newton's second law, the sum of forces on the planet is equal to the mass of the planet times its acceleration:

![lagrida_latex_editor (6)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/ba44c51a-3008-4d7f-910f-f97efe5daaec)



Substituting the gravitational force, we have:

This equation can be rearranged to solve for the acceleration vector $\vec{a}$:

�
⃗
=
−
�
�
�
3
�
⃗
a
 =− 
r 
3
 
GM
​
  
r
 

To numerically integrate the positions of the planet, we can define a state vector $\vec{x}(t)$:

�
⃗
(
�
)
=
[
�
(
�
)
�
(
�
)
�
(
�
)
�
�
(
�
)
�
�
(
�
)
�
�
(
�
)
]
x
 (t)= 
⎣
⎡
​
  
x(t)
y(t)
z(t)
v 
x
​
 (t)
v 
y
​
 (t)
v 
z
​
 (t)
​
  
⎦
⎤
​
 

This state vector contains the position and velocity components of the planet in three-dimensional space.

We can also define a function $f(\vec{x}, t)$ such that the derivative of the state vector is equal to $f(\vec{x}, t)$:

�
�
⃗
�
�
=
�
(
�
⃗
,
�
)
dt
d 
x
 
​
 =f( 
x
 ,t)

In this case, $f(\vec{x}, t)$ is given by:

�
(
�
⃗
,
�
)
=
[
�
�
(
�
)
�
�
(
�
)
�
�
(
�
)
−
�
�
�
(
�
)
�
3
−
�
�
�
(
�
)
�
3
−
�
�
�
(
�
)
�
3
]
f( 
x
 ,t)= 
⎣
⎡
​
  
v 
x
​
 (t)
v 
y
​
 (t)
v 
z
​
 (t)
r 
3
 
−GMx(t)
​
 
r 
3
 
−GMy(t)
​
 
r 
3
 
−GMz(t)
​
 
​
  
⎦
⎤
​
 

We can then use numerical integration methods to solve this system of differential equations and obtain the positions and velocities of the planet as functions of time.






