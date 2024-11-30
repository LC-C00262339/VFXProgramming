import bpy
import os
import sys
import importlib
from math import pi, radians

# Create objects

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object
cylinder.scale = (1, 1, 2)

bpy.ops.mesh.primitive_uv_sphere_add(location=(1, 0, 0), segments=6, ring_count=6, radius=0.75) # Create sphere
sphere = bpy.context.object

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 2), vertices=8, radius=1, depth=1) # Create octagonal prism using cylinder
octagon = bpy.context.object

bpy.ops.mesh.primitive_cone_add(location=(0, 0, 3), vertices=3, radius1=1, radius2=0, depth=2) # Create triangular prism
cone = bpy.context.object
