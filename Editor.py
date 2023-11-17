import dearpygui.dearpygui as dpg
import time

class Editor():
    def __init__ (self) -> None:
        self.console_buffer = ""

    def on_console_input(self, sender):
        input_text = dpg.get_value(sender)
        if (input_text):
            # Process the input_text here
            self.console_buffer += f">> {input_text.strip()}\n"
            # Update the output field with the new content
            dpg.set_value("Output", self.console_buffer)
            dpg.set_value(sender, "")  # Clear the input text

    def run(self):
        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()

        dpg.enable_docking(dock_space = True)

        with dpg.window(label="Entities"):
            pass
            
        with dpg.handler_registry():
            dpg.add_key_release_handler(callback=self.on_console_input)

        with dpg.window(label="Console"):
            # Console Output
            dpg.add_input_text(
                label="",
                default_value="UNIENGINE CONSOLE!",
                multiline=True,
                readonly=True,
                height=200,
                width=dpg.get_viewport_max_width(),
                tag="Output", # Assign an ID to the output field
            )
            # Console Input
            dpg.add_input_text( 
                label="",
                default_value="",
                height=50,
                width=dpg.get_viewport_max_width(),
                on_enter=True,
                callback=self.on_console_input,
            )

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

editor = Editor()
editor.run()
    
