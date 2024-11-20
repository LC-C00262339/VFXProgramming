import bpy

bpy.ops.primitive_cylinder.add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object
cylinder.scale (1, 1, 2)
