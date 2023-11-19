import dearpygui.dearpygui as dpg

class Windows:
    def __init__ (self) -> None:
        self.console_buffer = ""

    # Console Window
    def on_console_input(self, sender):
            input_text = dpg.get_value(sender)
            if (input_text):
                # Process the input_text here
                self.console_buffer += f">> {input_text.strip()}\n"
                # Update the output field with the new content
                dpg.set_value("Output", self.console_buffer)
                dpg.set_value(sender, "")  # Clear the input text
    def create_engine_console(self):
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

    # Entity Window
    def create_entity_window():
        with dpg.window(label="Entities") as EntitiesWindow:
            pass 
        dpg.set_item_height(EntitiesWindow, dpg.get_viewport_max_height())
        dpg.set_item_width(EntitiesWindow, 200)
        dpg.set_item_pos(EntitiesWindow, [0, 0])