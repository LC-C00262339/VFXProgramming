import bpy
import os
import sys
import importlib
from math import pi, radians

# Code should create a lighthouse

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object
cylinder.scale = (1, 1, 2)


bpy.ops.mesh.primitive_cone_add(location=(0, 0, 3.49), vertices=12, radius1=1.2, radius2=0.12, depth=1) # Create cone (roof)
cone = bpy.context.object

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 2.5), vertices=8, radius=0.9, depth=1) # Create octagonal prism using cylinder (inside)
window = bpy.context.object

# Add a few rocks with randomized fractals for roughness

bpy.ops.mesh.primitive_uv_sphere_add(location=(-1, 0, 0), vertices=8, rings=8, radius=0.75, name='ROCK')
rock = bpy.context.objects
rock.subdivide(number_cuts=1, fractal=3)

# Create object materials

material = bpy.data.materials.new(name='lighthouse') # Lighthouse building exterior 
# RGB = 1, 0.051, 0.040, 1
material.diffuse_color = (1.0, 0.051, 0.040, 1)
cylinder.data.materials.append(material) # Apply texture to cylinder

roof = bpy.data.materials.new(name='lightroof') # Lighthouse roof
# RGB = 0.05, 0.05, 0.05, 1
roof.diffuse_color = (0.050, 0.050, 0.050, 1)
roof.metallic = 0.7 # Add metallic shine to roof
roof.roughness = 0.75 # Affect how much light is diffused onto object

cone.data.materials.append(roof) # Apply texture to roof

# Add lighthouse light

bpy.ops.object.light_add(type='SPOT', location=(0, 0, 2.5), rotation=(0, radians(90), 0)) # Add spotlight
light = bpy.context.object 
light.data.energy = 500 # Power watt of light
