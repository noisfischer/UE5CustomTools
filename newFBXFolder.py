# Import the Unreal Engine Python API and the Tkinter library for GUI operations.
import unreal
import tkinter as tk
from tkinter import simpledialog

# Initialize the main Tkinter window.
ROOT = tk.Tk()

# Hide the main Tkinter window since we only need the dialog.
ROOT.withdraw()

# Open a simple dialog popup to ask the user for a folder name.
folderName = simpledialog.askstring(title="Folder Name", prompt="Name your folder:")

# Construct the main folder path by appending the user's folder name to a base path.
mainFolderPath = "/Game/SketchFabMeshes/" + folderName

# Construct a subfolder path that is based on the main folder path.
subFolderPath =  "/Game/SketchFabMeshes/" + folderName + "/"

# Define names for subfolders to organize textures and meshes.
textureFolder = "Textures"
meshFolder = "Mesh"

# Create the main folder and subfolders in Unreal Engine using the EditorAssetLibrary.
unreal.EditorAssetLibrary.make_directory(mainFolderPath)
unreal.EditorAssetLibrary.make_directory(subFolderPath + textureFolder)
unreal.EditorAssetLibrary.make_directory(subFolderPath + meshFolder)

# Check if the main directory was successfully created.
# If it exists, print a confirmation message in the Output Log.
if unreal.EditorAssetLibrary.does_directory_exist(mainFolderPath):
    print(f"Folder ({folderName}) Created!")
