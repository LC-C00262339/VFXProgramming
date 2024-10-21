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

start_frame = 1
mid_frame = 45
end_frame = 90

# Background

plane = cube_mesh.create_plane() 
plane.location = (-5, 0, 0)
plane.rotation_euler = (0, radians(90), 0)
console(f"Added background plane")

plane_b = cube_mesh.create_plane()
plane_b.location = (0, 0, -5)

# Top point

triangle_1 = cube_mesh.create_triangle()
triangle_1.location = (0, 0, 5)
# triangle_1.scale = (0.5, 0.5, 0.5)
console(f"Added triangle: {triangle_1.name}")

# Right bottom point


triangle_2 = cube_mesh.create_triangle()
triangle_2.location = (0, -5, -5)
# triangle_2.rotation_euler = (radians(90), 0, 0)
# triangle_2.scale = (0.5, 0.5, 0.5)
console(f"Added triangle: {triangle_2.name}")

# Left bottom point


# triangle_3 = cube_mesh.create_triangle()
# triangle_3.location = (0, -5, -5)
# console(f"Added triangle: {triangle_3.name}")

# Right middle point

triangle_4 = cube_mesh.create_triangle()
triangle_4.location = (0, 5, 0)
# triangle_4.rotation_euler = (radians(-90), 0, 0)
# triangle_4.scale = (0.5, 0.5, 0.5)
console(f"Added triangle: {triangle_4.name}")

# Left middle point

triangle_5 = cube_mesh.create_triangle()
triangle_5.location = (0, -5, 0)
# triangle_5.rotation_euler = (radians(90), 0, 0)
# triangle_5.scale = (0.5, 0.5, 0.5)
console(f"Added triangle: {triangle_5.name}")


# Top triangle animation

triangle_1.keyframe_insert("location", frame=start_frame) # Start
#triangle_1.keyframe_insert("scale", frame=start_frame)

triangle_1.location = (0, 0, 3) # 3 on Z axis at mid frame
# triangle_1.scale = (0.75, 0.75, 0.75)
triangle_1.keyframe_insert("location", frame=mid_frame) # Middle
#triangle_1.keyframe_insert("scale", frame=mid_frame)

triangle_1.location = (0, 0, 2) # 2 on Z axis at end frame
# triangle_1.scale = (1, 1, 1)
triangle_1.keyframe_insert("location", frame=end_frame)
#triangle_1.keyframe_insert("scale", frame=end_frame)

# Bottom triangle animation

triangle_2.rotation_euler = (0, 0, 0) # Rotation at start frame
# triangle_2.scale = (0.5, 0.5, 0.5)
triangle_2.keyframe_insert("location", frame=start_frame) # Start
triangle_2.keyframe_insert("rotation_euler", frame=start_frame)
#triangle_2.keyframe_insert("scale", frame=start_frame)

triangle_2.location = (0, -2.5, -3) # -2.5 on Y axis and -3 on Z axis at mid frame
triangle_2.rotation_euler = (radians(-90), 0, 0) # -90 rotation at mid frame
# triangle_2.scale = (0.75, 0.75, 0.75)
triangle_2.keyframe_insert("location", frame=mid_frame) # Middle
triangle_2.keyframe_insert("rotation_euler", frame=mid_frame)
#triangle_2.keyframe_insert("scale", frame=mid_frame)

triangle_2.location = (0, 0, -2) # -2 on Z axis at end frame
triangle_2.rotation_euler = (radians(-180), 0, 0) # -180 rotation at mid frame
# triangle_2.scale = (1, 1, 1)
triangle_2.keyframe_insert("location", frame=end_frame)
triangle_2.keyframe_insert("rotation_euler", frame=end_frame)
#triangle_2.keyframe_insert("scale", frame=end_frame)

# Left triangle animation


triangle_4.rotation_euler = (0, 0, 0) # Rotation at start frame
# triangle_4.scale = (0.5, 0.5, 0.5)
triangle_4.keyframe_insert("location", frame=start_frame) # Start
triangle_4.keyframe_insert("rotation_euler", frame=start_frame)
#triangle_4.keyframe_insert("scale", frame=start_frame)

triangle_4.location = (0, 3, 0) # 3 on Y axis at mid frame
# triangle_4.scale = (0.75, 0.75, 0.75)
triangle_4.rotation_euler = (radians(-45), 0, 0) # -45 rotation at mid frame
triangle_4.keyframe_insert("location", frame=mid_frame) # Middle
triangle_4.keyframe_insert("rotation_euler", frame=mid_frame)
#triangle_4.keyframe_insert("scale", frame=mid_frame)

triangle_4.location = (0, 2, 0) # 2 on Y axis at end frame
triangle_4.rotation_euler = (radians(-90), 0, 0) # -90 rotation at mid frame
# triangle_4.scale = (1, 1, 1)
triangle_4.keyframe_insert("location", frame=end_frame)
triangle_4.keyframe_insert("rotation_euler", frame=end_frame)
#triangle_4.keyframe_insert("scale", frame=end_frame)

# Right triangle anim

triangle_5.rotation_euler = (0, 0, 0) # Rotation at start frame
# triangle_5.scale = (0.5, 0.5, 0.5)
triangle_5.keyframe_insert("location",  frame=start_frame) # Start
triangle_5.keyframe_insert("rotation_euler", frame=start_frame)
#triangle_5.keyframe_insert("scale", frame=start_frame)

triangle_5.location = (0, -3, 0) # -3 on Y axis at mid frame
triangle_5.rotation_euler = (radians(45), 0, 0) # 45 rotation at mid frame
# triangle_5.scale = (0.75, 0.75, 0.75)
triangle_5.keyframe_insert("location", frame=mid_frame) # Middle
triangle_5.keyframe_insert("rotation_euler", frame=mid_frame)
#triangle_5.keyframe_insert("scale", frame=mid_frame)

triangle_5.location = (0, -2, 0) # -2 on Y axis at end frame
triangle_5.rotation_euler = (radians(90), 0, 0) # 90 rotation at mid frame
# triangle_5.scale = (1, 1, 1)
triangle_5.keyframe_insert("location", frame=end_frame)
triangle_5.keyframe_insert("rotation_euler", frame=end_frame)
#triangle_5.keyframe_insert("scale", frame=end_frame)

# The following code unwraps and wraps objects

# Top triangle

bpy.ops.object.select_all(action='DESELECT')
obj = bpy.data.objects['Triangle']
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
console(f"Object(s) unwrapped")

# Bottom triangle


bpy.ops.object.select_all(action='DESELECT')
obj = bpy.data.objects['Triangle.001']
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
console(f"Object(s) unwrapped")

# Left triangle

bpy.ops.object.select_all(action='DESELECT')
obj = bpy.data.objects['Triangle.002']
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
console(f"Object(s) unwrapped")

# Right triangle

bpy.ops.object.select_all(action='DESELECT')
obj = bpy.data.objects['Triangle.003']
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
console(f"Object(s) unwrapped")

# Planes


bpy.ops.object.select_all(action='DESELECT')
obj = bpy.data.objects['Plane']
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
console(f"Plane(s) unwrapped")


bpy.ops.object.select_all(action='DESELECT')
obj = bpy.data.objects['Plane.001']
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.mode_set(mode='OBJECT')
console(f"Plane(s) unwrapped")