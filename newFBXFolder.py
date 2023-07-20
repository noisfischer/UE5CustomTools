import unreal
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

# the input dialog
folderName = simpledialog.askstring(title="Folder Name", prompt="Name your folder:")

mainFolderPath = "/Game/SketchFabMeshes/" + folderName
subFolderPath =  "/Game/SketchFabMeshes/" + folderName + "/"

textureFolder = "Textures"
meshFolder = "Mesh"

unreal.EditorAssetLibrary.make_directory(mainFolderPath)
unreal.EditorAssetLibrary.make_directory(subFolderPath + textureFolder)
unreal.EditorAssetLibrary.make_directory(subFolderPath + meshFolder)

if unreal.EditorAssetLibrary.does_directory_exist(mainFolderPath):
    print(f"Folder ({folderName}) Created!")