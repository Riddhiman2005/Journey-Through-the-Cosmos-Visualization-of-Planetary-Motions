

The gravitational force on a planet with mass $m$ can be described by the equation

![lagrida_latex_editor (2)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/c18c75d0-a469-4a8e-a658-940252e7394a)

where G is the gravitational constant, M is the mass of the central object (the Sun in our case), ![lagrida_latex_editor (3)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/8cb0c954-d5b7-489e-9b26-db3f8252210f) is the position vector from the planet to the Sun, $r$ is the magnitude of the position vector, and ![lagrida_latex_editor (4)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/ca9ef961-3b7f-4e82-868d-269531d21e34) is the gravitational force vector.

By **Newton's second law**, *The sum of forces on the planet is equal to the mass of the planet times its acceleration*:

![lagrida_latex_editor (6)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/ba44c51a-3008-4d7f-910f-f97efe5daaec)


Substituting the gravitational force, we have:

![lagrida_latex_editor (7)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/893b9a00-47a2-4820-8b0e-8b4136f9e5d5)


This equation can be rearranged to solve for the acceleration vector ![lagrida_latex_editor (8)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/1ccdb566-9d21-4970-99f2-73d2b2f2ceb2):

We can find the velocity and position of the planet by integration as the acceleration of the planet is the derivative of the velocity and the double derivative of the position.

$$  \vec{a} = \vec{\dot v}  = \vec{\ddot r} $$

To numerically integrate the positions of the planet, we can define a state vector ![lagrida_latex_editor (2)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/02b6e330-94cf-4953-a1d7-f81d6209f553)

![lagrida_latex_editor (4)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/251dcf86-9823-4d19-92d5-df5f4a3f252f)




**This state vector contains the position and velocity components of the planet in three-dimensional space**.


We can also define a function $f(\vec{x}, t)$ such that the derivative of the state vector is equal to $f(\vec{x}, t)$:


![lagrida_latex_editor (2)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/c6fa9b3b-6f65-4db8-862b-3afb6a2f5763)


In this case, $f(\vec{x}, t)$ is given by:

![lagrida_latex_editor (3)](https://github.com/Riddhiman2005/Journey-Through-the-Cosmos-Visualization-of-Planetary-Motions/assets/130882317/4545de4b-d7fe-441c-adeb-e09746735a47)

 
We can then use numerical integration methods to solve this system of differential equations and obtain the positions and velocities of the planet as functions of time.






