# File Paramaters
BLENDER_BIN		:= blender					# name and location of blender binary // exe
BLEND_FILE		:= practical06scene		# Name of Blender File (Project file)
BLEND_SCRIPT	:= vfx_script.py			# Python Script to run

# Progress Messages
MSG_START	:= "Scene Build Started"
MSG_END		:= "Scene Build Complete"
MSG_CLEAN	:= "Cleaning up Directory"

build:
	@echo ${MSG_START}

	# Show Meshes
	${BLENDER_BIN} ${BLEND_FILE} -P ${BLEND_SCRIPT}