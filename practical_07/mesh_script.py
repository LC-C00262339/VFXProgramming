import bpy
import os
import sys
import importlib
from math import pi, radians

# Create objects

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(2, 2, 0), segments=6, ring_count=6, radius=0.75) # Create sphere
sphere = bpy.context.object

bpy.ops.mesh.primitive_cylinder_add(location=(0, -2, 0), vertices=8, radius=1, depth=1) # Create octagonal prism using cylinder
octagon = bpy.context.object

bpy.ops.mesh.primitive_cone_add(location=(0, 2, 0), vertices=3, radius1=1, radius2=0, depth=2) # Create triangular prism
cone = bpy.context.object


# Modifiers

modifiers = [
    {'name': 'Bevel', 'type': 'BEVEL', 'properties': {'affect': 'VERTICES', 'amount': 0.5, 'segments': 1}}, # Bevels cube mesh
    {'name': 'Build', 'type': 'BUILD', 'properties': {'frame_start': 10, 'frame_duration': 15}}, # Creates mesh during frames
    {'name': 'Mirror', 'type': 'MIRROR'}, # Mirror objects
    {'name': 'Subdivision', 'type': 'SUBSURF', 'properties': {'levels': 3}} # Subdivide
]