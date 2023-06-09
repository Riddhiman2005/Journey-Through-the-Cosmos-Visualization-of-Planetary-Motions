

import bpy
import math

# Function to create a planet
def create_planet(name, radius, distance, color):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=(distance, 0, 0))
    planet = bpy.context.object
    planet.name = name
    planet.data.materials.append(create_material(color))
    return planet

# Function to create a material with the given color
def create_material(color):
    material = bpy.data.materials.new(name=color)
    material.diffuse_color = color
    return material

# Function to create a sun
def create_sun(radius, color):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=(0, 0, 0))
    sun = bpy.context.object
    sun.name = 'Sun'
    sun.data.materials.append(create_material(color))
    return sun

# Function to animate the solar system
def animate_solar_system():
    scene = bpy.context.scene
    frames_per_revolution = 100

    # Define the properties of the planets
    planets = [
        {'name': 'Mercury', 'radius': 0.1, 'distance': 3, 'color': (0.7, 0.7, 0.7)},
        {'name': 'Venus', 'radius': 0.2, 'distance': 6, 'color': (0.9, 0.6, 0.1)},
        {'name': 'Earth', 'radius': 0.3, 'distance': 9, 'color': (0.1, 0.1, 0.9)},
        {'name': 'Mars', 'radius': 0.2, 'distance': 12, 'color': (0.9, 0.1, 0.1)},
        {'name': 'Jupiter', 'radius': 0.6, 'distance': 15, 'color': (0.8, 0.6, 0.3)},
        {'name': 'Saturn', 'radius': 0.5, 'distance': 18, 'color': (0.8, 0.8, 0.2)},
        {'name': 'Uranus', 'radius': 0.4, 'distance': 21, 'color': (0.4, 0.6, 0.8)},
        {'name': 'Neptune', 'radius': 0.4, 'distance': 24, 'color': (0.1, 0.1, 0.6)}
    ]

    # Create the sun
    sun = create_sun(1, (1, 1, 0.2))

    # Create the planets
    for planet_props in planets:
        planet = create_planet(**planet_props)
        bpy.ops.object.select_all(action='DESELECT')
        sun.select_set(True)
        planet.select_set(True)
        bpy.context.view_layer.objects.active = sun
        bpy.ops.object.parent_set(type='OBJECT')

        # Add animation to the planets
        bpy.ops.object.select_all(action='DESELECT')
        planet.select_set(True)
        bpy.context.view_layer.objects.active = planet
        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
        path = bpy.data.curves.new('Path', 'CURVE')
        path.dimensions = '3D'
        spline = path.splines.new('BEZIER')
        spline.bezier_points.add(frames_per_revolution)
        for i, point in enumerate(spline.bezier_points):
            angle = 2 * math.pi * i / frames_per_revolution
            point.co = (math.cos(angle) * planet_props['distance'], math.sin(angle) * planet_props['distance'], 0)
        planet.constraints['Follow Path'].target = path
        planet.constraints['Follow Path'].use_fixed_location = True
        planet.constraints['Follow Path'].forward_axis = 'FORWARD_X'
        planet.constraints['Follow Path'].up_axis = 'UP_Y'

    # Set up the animation settings
    scene.frame_start = 0
    scene.frame_end = frames_per_revolution
    scene.frame_current = 0
    bpy.ops.object.select_all(action='DESELECT')
    sun.select_set(True)
    bpy.context.view_layer.objects.active = sun
    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
    path = bpy.data.curves.new('Path', 'CURVE')
    path.dimensions = '3D'
    spline = path.splines.new('BEZIER')
    spline.bezier_points.add(frames_per_revolution)
    for i, point in enumerate(spline.bezier_points):
        angle = 2 * math.pi * i / frames_per_revolution
        point.co = (0, 0, 0)
    sun.constraints['Follow Path'].target = path
    sun.constraints['Follow Path'].use_fixed_location = True
    sun.constraints['Follow Path'].forward_axis = 'FORWARD_X'
    sun.constraints['Follow Path'].up_axis = 'UP_Y'

# Run the animation
animate_solar_system()
