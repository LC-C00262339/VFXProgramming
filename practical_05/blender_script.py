import random                       # Math Random
import bpy                          # Blender Python Module
import os                           # Operating System Module
import sys                          # System Module
import importlib                    # Importing Modules Module
from math import pi, radians        # Transformations Rotation


# Find out root directory of Blender Project
directory = os.path.dirname(bpy.data.filepath)
if not directory in sys.path:       # Check if this directory is in system Path
    sys.path.append(directory)      # Add Directory to Discoverable Path
   
import cube_mesh

import console_blender              # Import Custom Write to Console
importlib.reload(console_blender)   # Add custom module to the Blender Project (now that directory is know)
from console_blender import *       # After a reload import all the functions of the custom module

console("STARTS:")

# Set up frame increment

frames = 0
frame_increment = 5
offset = 10 # makes each object look a bit more dynamic

# Top point

triangle_1 = cube_mesh.create_triangle()
triangle_1.location = (0, 0, 5)
console(f"Added triangle: {triangle_1.name}")

# Right bottom point


triangle_2 = cube_mesh.create_triangle()
triangle_2.location = (0, 5, -5)
# triangle_2.rotation_euler = (radians(90), 0, 0)
console(f"Added triangle: {triangle_2.name}")

# Left bottom point


triangle_3 = cube_mesh.create_triangle()
triangle_3.location = (0, -5, -5)
console(f"Added triangle: {triangle_3.name}")

# Right middle point

triangle_4 = cube_mesh.create_triangle()
triangle_4.location = (0, 5, 0)
# triangle_4.rotation_euler = (radians(-90), 0, 0)
console(f"Added triangle: {triangle_4.name}")

# Left middle point

triangle_5 = cube_mesh.create_triangle()
triangle_5.location = (0, -5, 0)
# triangle_5.rotation_euler = (radians(90), 0, 0)
console(f"Added triangle: {triangle_5.name}")