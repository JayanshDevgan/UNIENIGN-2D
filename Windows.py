from Renderer import Renderer
import dearpygui.dearpygui as dpg
from Application import HUB_APP

class Windows:
    def __init__ (self) -> None:
        self.UNIENGINERenderer = Renderer()
        self.console_buffer = ""

    # Layouts
    def on_save_save_layout(self, sender) -> None:
            input_text = dpg.get_value(sender)
            if (input_text):
                pass
    def save_layout(self) -> None:
        with dpg.window(label="Save Layout") as SaveLayoutWindow:
            save_input_text = dpg.add_input_text(label="", default_value="", height=60, width=dpg.get_item_width(SaveLayoutWindow), callback=self.on_save_save_layout, on_enter=True)
            
            # Add a button parallel to the input text
            button_width = 100  # Adjust the width as needed
            dpg.add_same_line()  # Align elements horizontally
            dpg.add_button(label="Save", width=button_width, callback=lambda: self.on_save_save_layout(save_input_text))
    
    def set_default_layout() -> None:
        pass

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
                    dpg.add_input_text( label="", default_value="UNIENGINE CONSOLE!", multiline=True, readonly=True, height=200, width=dpg.get_viewport_max_width(), tag="Output") 
                    # Console Input
                    dpg.add_input_text(  label="", default_value="", height=50, width=dpg.get_viewport_max_width(), callback=self.on_console_input, on_enter=True)
    # WORLD SPACE Window
    def create_worldspace_window(self) -> None:
        with dpg.window(label="World Space", height=dpg.get_viewport_max_height() / 2.5, width=dpg.get_viewport_max_width() / 1.5, pos=[300, 300]):
            self.UNIENGINERenderer.render()
          
    # Entity Window
    def create_entity_window(self) -> None:
        with dpg.window(label="Entities", height=dpg.get_viewport_max_height(), width=200, pos=[0, 0]):
            pass
