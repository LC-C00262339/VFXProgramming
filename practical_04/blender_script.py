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

# Triangle
triangleside1 = bpy.context.scene.objects["TriangleSide1"]
triangleside2 = bpy.context.scene.objects["TriangleSide2"]
triangleside3 = bpy.context.scene.objects["TriangleSide3"]

# Triangle bottom formation 

triangleside3.keyframe_insert("location", frame=start_frame)
triangleside3.location.x = 1.7
triangleside3.location.z = 1.5
triangleside3.rotation_euler = (0.2, 0, 0)
console(f"Triangle base moved and rotated")

triangleside3.keyframe_insert("location", frame=mid_frame)
triangleside3.rotation_euler = (0.7, 0, 0)
triangleside3.location.x = 2.5
triangleside3.location.z = 3.5

triangleside3.keyframe_insert("location", frame=end_frame)
triangleside3.rotation_euler = (1.58, 0, 0)
triangleside3.location.x = 3.9
triangleside3.location.z = 5

# Triangle left rotation

triangleside2.keyframe_insert("location", frame=start_frame)
triangleside2.location.x = -2.5
triangleside2.location.z = 1.5
triangleside2.rotation_euler = (0.2, 0, 0)

triangleside2.keyframe_insert("location", frame=mid_frame)
triangleside2.location.x = -1
triangleside2.location.z = 3.5
triangleside2.rotation_euler = (0.25, 0, 0)

triangleside2.keyframe_insert("location", frame=end_frame)
triangleside2.rotation_euler = (0.45, 0, 0)
triangleside2.location.x = 3.9
triangleside2.location.y = 0.5
triangleside2.location.z = 6

# Triangle right rotation

triangleside1.keyframe_insert("location", frame=start_frame)
triangleside1.location.x = -2.5
triangleside1.location.z = 1.5
triangleside1.rotation_euler = (-0.2, 0, 0)

triangleside1.keyframe_insert("location", frame=mid_frame)
triangleside1.location.x = -1
triangleside1.location.z = 3.5
triangleside1.rotation_euler = (-0.25, 0, 0)

triangleside1.keyframe_insert("location", frame=end_frame)
triangleside1.rotation_euler = (-0.45, 0, 0)
triangleside1.location.x = 3.9
triangleside1.location.y = -0.5
triangleside1.location.z = 6


# Arm rotation
arml.keyframe_insert("location", frame=start_frame)
console(f"Left arm rotated down")
arml.rotation_euler = (-0.2, 0, 0)
arml.keyframe_insert("location", frame=mid_frame)
arml.rotation_euler = (0, 0, 0)
console(f"Left arm moving upwards")
arml.keyframe_insert("location", frame=end_frame)
arml.rotation_euler = (0.2, 0, 0)
console(f"Left arm rotated up")

armr.keyframe_insert("location", frame=start_frame)
console(f"Right arm rotated down")
armr.rotation_euler = (0.2, 0, 0)
armr.keyframe_insert("location", frame=mid_frame)
armr.rotation_euler = (0, 0, 0)
console(f"Right arm moving upwards")
armr.keyframe_insert("location", frame=end_frame)
armr.rotation_euler = (-0.2, 0, 0)
console(f"Right arm rotated up")

