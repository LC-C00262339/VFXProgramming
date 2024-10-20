import bpy

# Cube = 8 vertices, 6 faces, 12 edges
# Pyramid = 6 vertices, 5 faces, 9 edges

# Vertices are orderered?

vertices = [
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, -1),
    (-1, 1, 1),
    (1, -1, -1),
    (1, -1, 1),
    (1, 1, -1),
    (1, 1, 1)
]

edges = [
    ((-1, -1, -1), (-1, -1, 1)),
    ((-1, -1, -1), (-1, 1, -1)),
    ((-1, -1, -1), (1, -1, -1)),
    ((-1, -1, 1), (-1, 1, 1)),
    ((-1, -1, 1), (1, -1, 1)),
    ((-1, 1, -1), (-1, 1, 1)),
    ((-1, 1, -1), (1, 1, -1)),
    ((1, -1, -1), (1, -1, 1)),
    ((1, -1, -1), (1, 1, -1)),
    ((-1, 1, 1), (1, 1, 1)),
    ((1, -1, 1), (1, 1, 1)),
    ((1, 1, -1), (1, 1, 1))
]

faces = [
    [0, 1, 3, 2],  # Left face
    [4, 5, 7, 6],  # Right face
    [0, 1, 5, 4],  # Bottom face
    [2, 3, 7, 6],  # Top face
    [0, 2, 6, 4],  # Front face
    [1, 3, 7, 5]   # Back face
]

triangle_vertices = [ 
    (-1, -1, -1),
    (-1, 0, 1),
    (-1 ,1, -1),
    (1, -1, -1),
    (1, 0, 1),
    (1, 1, -1)
]

#triangle_edges = [
#    ((-1, -1, -1), (-1, -1, 1)),
#    ((-1, 0, -1), (-1, 0, 1)),
#   ((-1, -1, -1), (-1, 1, -1)),
#    ((1, -1, -1))
#]

# Edges are likely not needed

triangle_faces = [ 
    [4, 5, 2], 
    [1, 0, 3],
    [2, 5, 3],
    [4, 3, 5],
    [1, 2, 0],
    [1, 4, 2],
    [4, 1, 3],
    [0, 2, 3] 
]

plane_vertices = [
    (-5, 5, 0),
    (5, 5, 0),
    (5, -5, 0),
    (-5, -5, 0)
]

plane_faces = [
    [0, 1, 2, 3]
]

def print_cube():
    # Output the cube definition
    print("Cube Vertices:")
    for vertex in vertices:
        print(vertex)

    print("\nCube Edges:")
    for edge in edges:
        print(f"{edge[0]} to {edge[1]}")

    print("\nCube Faces:")
    for face in faces:
        print(" → ".join(map(str, [vertices[i] for i in face])))

def create_cube():
    # Create a new mesh and object
    mesh = bpy.data.meshes.new('Custom Cube Mesh')
    obj = bpy.data.objects.new('Custom Cube Object', mesh)

    # Link the object to the scene
    bpy.context.collection.objects.link(obj)

    # Create the mesh from the vertices and faces
    mesh.from_pydata(vertices, [], faces)
    mesh.update()

    return obj

# Triangle mesh creation

def print_triangle():
    print("Triangle vertices:")
    for vertex in triangle_vertices:
        print(vertex)

    print("\nTriangle Faces:")
    for face in triangle_faces:
        print(" → ".join(map(str, [triangle_vertices[i] for i in face])))

def create_triangle():
    mesh = bpy.data.meshes.new('Triangle')
    obj = bpy.data.objects.new('Triangle', mesh)

    bpy.context.collection.objects.link(obj)

    mesh.from_pydata(triangle_vertices, [], triangle_faces)
    mesh.update()

    return obj

def print_plane():
    print("Plane vertices:")
    for vertex in plane_vertices:
        print(vertex)

    print("\nPlane faces:")
    for face in plane_faces:
        print(" → ".join(map(str, [plane_vertices[i] for i in face])))

def create_plane():
    mesh = bpy.data.meshes.new('Plane')
    obj = bpy.data.objects.new('Plane', mesh)

    bpy.context.collection.objects.link(obj)

    mesh.from_pydata(plane_vertices, [], plane_faces)
    mesh.update()
    
    return obj