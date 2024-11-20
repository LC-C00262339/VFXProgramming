import bpy

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object
cylinder.scale = (1, 1, 2)


bpy.ops.mesh.primitive_cone_add(location=(0, 0, 4), vertices=12, radius1=1.5, radius2=0) # Create cone (roof)