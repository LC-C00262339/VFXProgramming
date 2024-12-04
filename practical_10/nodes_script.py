import bpy
import os
import sys
import importlib
import math


nodes_name = 'GeometryNodes'

object = bpy.context.object

translate_obj = 'Translation'
scale_obj = 'Scale'
rotate_obj = 'Rotate'

modifier = object.modifiers[nodes_name] # Modifier for nodes

node_group = modifier.node_group

nodes = node_group.nodes

# Create meshes

bpy.ops.mesh.primitive_cube_add(location=(0, 4, 4))
cube = bpy.context.object
bpy.ops.object_modifier_add(type='NODES')
cube_nodes = cube.modifiers["GeometryNodes"]


bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 2, 2), segments=6, ring_count=6)
sphere = bpy.context.object
bpy.ops.object_modifier_add(type='NODES')
sphere_nodes = sphere.modifiers["GeometryNodes"]



for node in nodes:
    if(node.label == translate_obj):
        node.vector = (2.0, 2.0, 2.0)
    if(node.label == rotate_obj):
        node.rotation_euler=(0.0, 0.0, 0.0)
    if(node.label == scale_obj):
        node.vector = (1.0, 1.0, 1.0)

object.data.update()