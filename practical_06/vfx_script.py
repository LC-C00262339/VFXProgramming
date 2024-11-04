import bpy
import sys
import importlib
from math import pi, radians

bpy.ops.primitive_cube_add(location=(0,1,0))
bpy.ops.primitive_cone_add(location=(0,2,0))
bpy.ops.primitive_uv_sphere_add(segments=8, ring_count=8, radius=1.0, location=(0,3,0))
