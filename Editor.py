import dearpygui.dearpygui as dpg
from Windows import Windows

class Editor():
    def __init__ (self) -> None:
        self.console_buffer = ""

    def run(self):
        dpg.create_context()
        dpg.create_viewport(title="UNIENGINE-2D")
        dpg.setup_dearpygui()

        dpg.configure_app(docking=True, docking_space=True)

        with dpg.viewport_menu_bar():
            with dpg.menu(label="Windows"):
                dpg.add_menu_item(label="Engine Console", callback=Windows.create_engine_console)
                dpg.add_menu_item(label="Entity Window", callback=Windows.create_entity_window)

        Windows.create_entity_window()

        with dpg.handler_registry():
            dpg.add_key_release_handler(callback=self.on_console_input)

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

editor = Editor()
editor.run()
    
