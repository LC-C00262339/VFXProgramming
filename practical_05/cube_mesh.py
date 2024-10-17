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
