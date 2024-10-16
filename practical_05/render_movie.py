import bpy                          # Blender Python Module
import sys                          # System Module
import os                           # Operating System Module

# Get the output directory, movie output path, and frame range from command line arguments
output_dir = sys.argv[-3]  # Third last argument
movie_output = sys.argv[-2]  # Second last argument
frame_range = sys.argv[-1]    # Last argument, e.g. "1..100"

# Split the frame range into start and end frames
start_frame, end_frame = map(int, frame_range.split('..'))

# Set the frame range in Blender
bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

# Ensure the sequence editor exists
if not bpy.context.scene.sequence_editor:
    bpy.context.scene.sequence_editor_create()

# Clear existing strips if necessary
sequence_editor = bpy.context.scene.sequence_editor
for strip in sequence_editor.sequences:
    sequence_editor.sequences.remove(strip)

# Check if output directory exists and has PNG files
if not os.path.exists(output_dir):
    raise Exception(f"Output directory does not exist: {output_dir}")

# List PNG files in the output directory
image_files = sorted([f for f in os.listdir(output_dir) if f.endswith('.png')])
if not image_files:
    raise Exception(f"No PNG files found in the directory: {output_dir}")

# Add Image Strips only for the specified frame range using absolute paths
for i, image_file in enumerate(image_files):
    frame_number = start_frame + i  # Calculate the frame number
    if frame_number > end_frame:
        break  # Stop if the frame number exceeds the end frame
    full_path = os.path.abspath(os.path.join(output_dir, image_file))  # Use absolute path
    # Use `bpy.data` to add an image strip without the context
    strip = sequence_editor.sequences.new_image(
        name=image_file,
        filepath=full_path,
        channel=1,  # Set the channel to 1 (you can adjust as needed)
        frame_start=frame_number  # Start at the calculated frame number
    )

# Set output settings
bpy.context.scene.render.filepath = movie_output
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'

# Render the animation
bpy.ops.render.render(animation=True)

# Save the Blender file (optional, can be removed if not needed)
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

# Close Blender
bpy.ops.wm.quit_blender()
