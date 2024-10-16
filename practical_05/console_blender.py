import bpy

def console(info):
    """
    Get the window context
    Get the Screen
    Get the Area Type
    Append to Console
    """
    # Iterate over all windows
    for window in bpy.context.window_manager.windows:
        # Get the screen of the current window
        screen = window.screen
        # Iterate over all areas of the screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                # Get the correct context for the operator
                with bpy.context.temp_override(window=window, area=area):
                    bpy.ops.console.scrollback_append(text=str(info), type='OUTPUT')