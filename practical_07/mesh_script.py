import bpy
import os
import sys
import importlib
import math

# Animation function

def animate_object(obj, frame, location=None, rotation=None, scale=None):
    if location:
        obj.rotation = location
        obj.keyframe_insert(data_path="location", frame=frame)
    if rotation:
        obj.rotation_euler = rotation
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)
    if scale:
        obj.scale = scale
        obj.keyframe_insert(data_path="scale", frame=frame)

# Create objects

bpy.ops.mesh.primitive_cube_add(location=(0, 1, 1)) # Create cube
cube = bpy.context.object

bpy.ops.mesh.primitive_cube_add(location=(-2.6, 0, 2.4), scale=(0.1, 5, 2.5))
top = bpy.context.object

bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0, math.radians(90), 0), scale=(0.1, 5, 2.5))
bottom = bpy.context.object


bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(2, 2, 0), segments=6, ring_count=6, radius=0.75) # Create sphere
sphere = bpy.context.object

bpy.ops.mesh.primitive_cylinder_add(location=(0, -2, 0), vertices=8, radius=1, depth=1) # Create octagonal prism using cylinder
octagon = bpy.context.object

bpy.ops.mesh.primitive_cone_add(location=(0, 2, 0), vertices=3, radius1=1, radius2=0, depth=2) # Create triangular prism
cone = bpy.context.object

bpy.ops.object.light_add(type='SPOT', location=(0, 0, 2.5))
light = bpy.context.object 
light.data.energy = 500 # Power watt of light

# Create frames

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 150


# Modifiers

modifiers = [
    {'name': 'Array', 'type': 'ARRAY', 'properties': {'count': 3, 'relative_offset_displace': (2, 0, 0)}}, # Duplicate object
    {'name': 'Bevel', 'type': 'BEVEL', 'properties': {'affect': 'VERTICES', 'amount': 0.5, 'segments': 1}}, # Bevels cube mesh
    {'name': 'Build', 'type': 'BUILD', 'properties': {'frame_start': 10, 'frame_duration': 15}}, # Creates mesh during frames
    {'name': 'Mirror', 'type': 'MIRROR'}, # Mirror objects
    {'name': 'Subdivision', 'type': 'SUBSURF', 'properties': {'levels': 3}} # Subdivide
]

# Animation

animate_object(sphere, frame=1, location=(2, 2, 0), rotation=(0, 0, 0), scale=(1, 1, 1))
animate_object(sphere, frame=50, location=(2, 4, 0), rotation=(0, 0, 0), scale=(1, 1, 1))
