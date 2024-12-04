import bpy
import os
import sys
import importlib
import math

#os.getcwd()
#directory = os.path.dirname(bpy.data.filepath)
# if not directory in sys.path:
  #  sys.path.append(directory)

# Animation function

def animate_object(obj, frame, location=None, rotation=None, scale=None):
    if location:
        obj.location = location
        obj.keyframe_insert(data_path="location", frame=frame)
    if rotation:
        obj.rotation_euler = rotation
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)
    if scale:
        obj.scale = scale
        obj.keyframe_insert(data_path="scale", frame=frame)

# Create camera

bpy.ops.object.camera_add(location=(8, -12, 6), rotation=(math.radians(75), 0, math.radians(30)))
camera = bpy.context.object 
bpy.context.scene.camera = camera 

# Create objects

bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1)) # Create cube
cube = bpy.context.object
bpy.ops.object.editmode_toggle()
bpy.ops.uv.unwrap(method='ANGLE_BASED')
bpy.ops.object.editmode_toggle()

bpy.ops.mesh.primitive_cube_add(location=(-2.6, 0, 3), scale=(0.1, 10, 3))
top = bpy.context.object

bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), rotation=(0, math.radians(90), 0), scale=(0.1, 10, 2.5))
bottom = bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 1.5, 3), segments=6, ring_count=6, radius=0.75) # Create sphere
sphere = bpy.context.object

bpy.ops.mesh.primitive_cylinder_add(location=(0, 3, 3), rotation=(math.radians(90), 0, 0), vertices=8, radius=1, depth=1) # Create octagonal prism using cylinder
octagon = bpy.context.object

bpy.ops.mesh.primitive_cone_add(location=(0, 3, 1.1), vertices=3, radius1=1, radius2=0, depth=2) # Create triangular prism
cone = bpy.context.object

bpy.ops.object.light_add(type='SPOT', location=(0, 0, 10))
light = bpy.context.object 
light.data.energy = 500 # Power watt of light

# Create frames

bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 150


# Object materials/textures

cubetexture = bpy.data.materials.new(name="cube_texture")
cubetexture.use_nodes = True
nodes = cubetexture.node_tree.nodes
texture_node = nodes.new("ShaderNodeTexImage")
texture_node.image = bpy.data.images.load("/practical_09/textures/polkadottexture.png")
cube.data.materials.append(cubetexture)


# Animation

animate_object(sphere, frame=1, location=(0, -3, 3), rotation=(0, 0, 0), scale=(1, 1, 1))
animate_object(sphere, frame=50, location=(1, -1.5, 2.5), rotation=(0, 0, 0), scale=(1, 1, 1))
animate_object(sphere, frame=100, location=(1, 1.5, 3), rotation=(0, 0, 0), scale=(1, 1, 1))
animate_object(sphere, frame=150, location=(1, 3, 3.5), rotation=(0, 0, 0), scale=(1, 1, 1))

animate_object(cone, frame=1, location=(0, 5, 1.1), rotation=(0, 0, 0), scale=(1, 1, 1))
animate_object(cone, frame=50, location=(0, 5, 1.1), rotation=(0, 0, math.radians(90)), scale=(1, 1, 1))
animate_object(cone, frame=100, location=(0, 5, 1.1), rotation=(0, 0, math.radians(180)), scale=(1, 1, 1))
animate_object(cone, frame=150, location=(0, 5, 1.1), rotation=(0, 0, math.radians(90)), scale=(1, 1, 1))

animate_object(octagon, frame=1, location=(0, 3, 3), rotation=(0, 0, 0), scale=(1, 1, 1))
animate_object(octagon, frame=50, location=(0, 3, 3), rotation=(0, 0, math.radians(90)), scale=(1, 1, 1))
animate_object(octagon, frame=100, location=(0, 3, 3), rotation=(0, 0, math.radians(45)), scale=(1, 1, 1))
animate_object(octagon, frame=150, location=(0, 3, 3), rotation=(0, 0,0), scale=(1, 1, 1))

animate_object(camera, frame=1, location=(8, -12, 6), rotation=(math.radians(75), 0, math.radians(30)), scale=(1, 1, 1))
animate_object(camera, frame=50, location=(12, -5.8, 5.9), rotation=(math.radians(75), 0, math.radians(60)), scale=(1, 1, 1))
animate_object(camera, frame=100, location=(12, 2, 5), rotation=(math.radians(75), 0, math.radians(90)), scale=(1, 1, 1))