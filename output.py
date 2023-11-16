from colorama import Fore
from customtkinter import CTkCanvas
class UNIConsole:
    def __init__(self) -> None:
        pass

    def Error(Canvas: CTkCanvas, posX: int, posY: int, msg: str) -> None:
        Canvas.create_text(posX, posY, text=msg, fill="lightred")
        Canvas.pack(fill="both", expand=True)
        # print(Fore.LIGHTRED_EX, msg, Fore.WHITE)
    
    def Warn(Canvas: CTkCanvas, posX: int, posY: int, msg: str) -> None:
        Canvas.create_text(posX, posY, text=msg, fill="lightyellow")
        Canvas.pack(fill="both", expand=True)
        # print(Fore.LIGHTYELLOW_EX, msg, Fore.WHITE)
    
    def Success(Canvas: CTkCanvas, posX: int, posY: int, msg: str) -> None:
        Canvas.create_text(posX, posY, text=msg, fill="lightgreen")
        Canvas.pack(fill="both", expand=True)
        # print(Fore.LIGHTGREEN_EX, msg, Fore.WHITE)

class UNI:
    def __init__(self) -> None:
        pass

    def Error(msg: str) -> None:
        print(Fore.LIGHTRED_EX, msg, Fore.WHITE)
    
    def Warn(msg: str) -> None:
        print(Fore.LIGHTYELLOW_EX, msg, Fore.WHITE)
    
    def Success(msg: str) -> None:
        print(Fore.LIGHTGREEN_EX, msg, Fore.WHITE)