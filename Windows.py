import dearpygui.dearpygui as dpg

class Windows:
    def __init__ (self) -> None:
        self.console_buffer = ""

    # Console Window
    def on_console_input(self, sender) -> None:
            input_text = dpg.get_value(sender)
            if (input_text):
                # Process the input_text here
                self.console_buffer += f">> {input_text.strip()}\n"
                # Update the output field with the new content
                dpg.set_value("Output", self.console_buffer)
                dpg.set_value(sender, "")  # Clear the input text
    def create_engine_console(self) -> None:
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
                        callback=self.on_console_input,
                        on_enter=True,
                    )

    def create_worldspace_window():
          with dpg.window(label="World Space", height=dpg.get_viewport_max_height() / 2.5, width=dpg.get_viewport_max_width() / 1.5, pos=[300, 300]):
                pass
          
    def create_entity_window() -> None:
        with dpg.window(label="Entities", height=dpg.get_viewport_max_height(), width=200, pos=[0, 0]):
            pass
