import dearpygui.dearpygui as dpg
from Windows import Windows

class Editor:
    def __init__ (self) -> None:
        self.windows = Windows()
        

    def run(self) -> None:
        dpg.create_context()
        dpg.create_viewport(title="UNIENGINE", small_icon="./images/UNI_Light.ico")
        dpg.setup_dearpygui()

        dpg.configure_app(docking=True, docking_space=True)

        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                pass
            with dpg.menu(label="Windows"):
                dpg.add_menu_item(label="Engine Console", callback=self.windows.create_engine_console)
                dpg.add_menu_item(label="Entity Window", callback=self.windows.create_entity_window)
            with dpg.menu(label="Layout"):
                dpg.add_menu_item(label="Default Layout", callback=self.windows.set_default_layout)
                dpg.add_separator()
                dpg.add_menu_item(label="Save Layout", callback=self.windows.save_layout)

        self.windows.create_entity_window()
        self.windows.create_worldspace_window()

        with dpg.handler_registry():
            dpg.add_key_release_handler(callback=self.windows.on_console_input)

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

editor = Editor()
editor.run()
    
