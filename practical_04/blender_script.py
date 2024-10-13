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

import console_blender              # Import Custom Write to Console
importlib.reload(console_blender)   # Add custom module to the Blender Project (now that directory is know)
from console_blender import *       # After a reload import all the functions of the custom module

console("STARTS:")

start_frame = 1
mid_frame = 45
end_frame = 90

# Suzanne
suzanne = bpy.context.scene.objects["Suzanne"]
suzannebody = bpy.context.scene.objects["SuzanneBody"]
arml = bpy.context.scene.objects["ArmL"]
armr = bpy.context.scene.objects["ArmR"]

# Triangle formation
triangleside1 = bpy.context.scene.objects["TriangleSide1"]
triangleside2 = bpy.context.scene.objects["TriangleSide2"]
triangleside3 = bpy.context.scene.objects["TriangleSide3"]

triangleside3.keyframe_insert("location", frame=start_frame)
console(f"Triangle base moved and rotated")
triangleside3.keyframe_insert("location", frame=mid_frame)
triangleside3.location.z = 1.5
triangleside3.rotation_euler = (0.2, 0, 0)
