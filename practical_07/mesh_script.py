import bpy

# Code should create a lighthouse

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 0), vertices=12) # Create cylinder
cylinder = bpy.context.object
cylinder.scale = (1, 1, 2)


bpy.ops.mesh.primitive_cone_add(location=(0, 0, 3.49), vertices=12, radius1=1.2, radius2=0.12, depth=1) # Create cone (roof)
cone = bpy.context.object

bpy.ops.mesh.primitive_cylinder_add(location=(0, 0, 2.5), vertices=8, radius=0.9, depth=1) # Create octagonal prism using cylinder (inside)
window = bpy.context.object

# bpy.ops.mesh.primitive_cube_add(location=(0, 0, 3.5) # Create cube (inside)
# cube = bpy.context.object