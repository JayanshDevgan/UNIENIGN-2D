from customtkinter import filedialog
from output import UNI
import customtkinter
import winreg
import shutil
import ctypes
import os

## GLOBAL FUNCTIONS

def CreateUNIBATFile(ProjectLocation: str, ProjectName: str) -> None:
    try:
        os.makedirs(f"{os.path.join(ProjectLocation, ProjectName)}/core/editor", exist_ok=True)
        with open(f"{os.path.join(ProjectLocation, ProjectName)}/core/editor/Editor.py", 'x') as EDITORFILE:
            pass
        # To copy content from existing editor.py to the new editor.py
        with open('./Editor.py', 'r') as EditorFile:
            content = EditorFile.read()
            with open(f"{os.path.join(ProjectLocation, ProjectName)}/core/editor/Editor.py", 'w') as NewEditorFile:
                NewEditorFile.write(content)
        # To copy content from existing output.py to the new output.py
        with open('./output.py', 'r') as OutputFile:
            content = OutputFile.read()
            with open(f"{os.path.join(ProjectLocation, ProjectName)}/core/editor/output.py", 'w') as NewOutputFile:
                NewOutputFile.write(content)
                
        os.makedirs(f"{ProjectLocation}/{ProjectName}/core/public/", exist_ok=True)
        shutil.copy('./images/UNIBATFILEicon.ico', f"{ProjectLocation}/{ProjectName}/core/public/")
        shutil.copy('./images/UNI_Dark.ico', f"{ProjectLocation}/{ProjectName}/core/public/")

        ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", f'"{os.path.abspath(__file__)}"', None, 1) ## Giving ADMIN RIGHTS

        try:
            file_extension = ".UNI.bat"
            python_script = f"{ProjectLocation}/{ProjectName}/core/editor/editor.py"
            icon_path = f"{ProjectLocation}/{ProjectName}/core/public/UNIBATFILEicon.ico"

            try:
                with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_extension) as UNIBAT_KEY:
                    winreg.SetValue(UNIBAT_KEY, "DefaultIcon", winreg.REG_SZ, icon_path)
                    command_key = winreg.CreateKey(UNIBAT_KEY, r"shell\open\command")
                    winreg.SetValue(command_key, "", winreg.REG_SZ, f'python "{python_script}" "%1"')
            except Exception as error:
                UNI.Error(f"Exception Error - {ProjectName}: {type(error)} -> {str(error)}")
        except Exception as error:
            UNI.Error(f"Exception Error - {ProjectName}: {type(error)} -> {str(error)}")

    except Exception as error:
        UNI.Error(f"Exception Error - {ProjectName}: {type(error)} -> {str(error)}")

def CreateProject(ProjectName: str, ProjectLocation: str) -> None:
        AllowedCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        UNI.Success(f"Creating {{{ProjectName}}} at \n\t\t {ProjectLocation}")
        if all(char in AllowedCharacters for char in ProjectName) and len(ProjectName) >= 3:
            try:
                os.mkdir(path=os.path.join(ProjectLocation, ProjectName))
                # CREATE A .UNIBAT FILE TO RUN OUR PROJECT
                try:
                    ProjectUNIBAT_File = open(f"{ProjectLocation}/{ProjectName}/{ProjectName}.UNI.bat", 'w+')
                    ProjectUNIBAT_File.write(f'''
                                            @echo off
                                            pip install customtkinter
                                            python "{ProjectLocation}/{ProjectName}/core/editor/Editor.py"
                                            pause
                                                ''')
                    ProjectUNIBAT_File.close()
                except FileExistsError as FEerror:
                    UNI.Error(f"Project Name - {ProjectName} -> File Exists Error: {FEerror}")
                
                # UNIBAT FILE CODE
                CreateUNIBATFile(ProjectLocation=ProjectLocation, ProjectName=ProjectName)
                UNI.Success("Project Created Successfully at {}".format((os.path.join(ProjectLocation, ProjectName)).replace('\\', '/')))
                os.startfile(os.path.join(ProjectLocation, ProjectName))
                root.destroy()
            except Exception as error:
                UNI.Error(f"Exception Error - {ProjectName}: {type(error)} -> {str(error)}")
        else:
            UNI.Error(f"Project Name - {ProjectName} -> Invalid Name \n\t\t Only A-Z, a-z, and _ are allowed \n\t\t\t\tor\n\t\t\t Project Name is too shot")


class HUB_APP:
    def __init__(self) -> None:
        pass

    def Application() -> None:
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        
        global root
        root = customtkinter.CTk()
        root.geometry("500x350")
        root.iconbitmap("./images/UNI_Dark.ico")
        root.title("UNI ENGINE HUB")

        UNI.Success("Application Booted")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="UNI ENGINE")
        label.pack(pady=12, padx=10)

        def SelectProjectLocation() -> str:
            path = filedialog.askdirectory(title="Browse Project Directory")
            return path
        
        def ProjectLocationButton() -> None:
            global _path_
            _path_ = SelectProjectLocation()

        global ProjectName
        ProjectName = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Project Name")
        ProjectName.pack(pady=12, padx=10)
        ProjectLocationBtn = customtkinter.CTkButton(master=frame, text="Browse Project Location", command=ProjectLocationButton)
        ProjectLocationBtn.pack(pady=12, padx=10)
        
        def CreateProjectButton() -> None:
            CreateProject(ProjectName=ProjectName.get(), ProjectLocation=_path_)

        CreateProjectBtn = customtkinter.CTkButton(master=frame, text="Create Project", command=CreateProjectButton)
        CreateProjectBtn.pack(pady=12, padx=10)

        def ExitHubButton() -> None:
            try:
                 UNI.Warn("\n\t\t\t\t Exiting UNI ENGINE HUB")
                 root.destroy()
            except BaseException as BEError:
                 UNI.Error(f"Exception Error: {BEError}")

        HUBExitBtn = customtkinter.CTkButton(master=frame, text="EXIT", fg_color="Maroon", hover_color="#610c04", command=ExitHubButton)
        HUBExitBtn.pack(pady=12, padx=10)

        root.mainloop()