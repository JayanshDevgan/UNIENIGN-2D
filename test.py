import dearpygui.dearpygui as dpg

def create_docked_windows():
    with dpg.dockspace():
        # Create a dock space
        with dpg.dock(title="DockSpace"):
            # Dock your windows into the central dock space
            with dpg.dock(id=1, slot=0):
                with dpg.window(label="Window 1"):
                    pass

            with dpg.dock(id=2, slot=1):
                with dpg.window(label="Window 2"):
                    pass

            with dpg.dock(id=3, slot=2):
                with dpg.window(label="Window 3"):
                    pass

with dpg.create_viewport(title="UNIENGINE"):
    create_docked_windows()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

