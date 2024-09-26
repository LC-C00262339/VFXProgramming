# Practical 02 - CRUD
# Script adds and removes cubes to Blender following the Create, Read, Update and Delete (CRUD) operations.

import csv
import os
import bpy

os.system('cls' if os.name == 'nt' else 'clear')

stage_scene_one_file = "scene.csv"
stage_set_data = []

# Read File
try:
    print(f"Opening File {stage_scene_one_file} to read")
    scene_one = open(stage_scene_one_file, "r", newline='') # read mode
    csv_reader = csv.reader(scene_one)
except:
    print(f"There was an error opening {stage_scene_one_file}")
else:
    for props in csv_reader: # loop through file
        bpy.ops.mesh.primitive_cube_add(location=(stage_scene_one_file))
        stage_set_data.append("2.0, -2.0, 2.0,")
    print(stage_set_data)
    scene_one.close() # close the file
finally:
    print(f"Finally {stage_scene_one_file}")

