import unreal

# Get the current editor world
editor_world = unreal.EditorLevelLibrary.get_editor_world()

# Access the Level Editor Subsystem to interact with the editor's level-related functionalities.
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

# Retrieve current camera position and rotation from the editor's viewport.
viewport = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()

# Extract the camera's location and rotation from the viewport information.
cameraLocation = viewport[0]
cameraRotation = viewport[1]

# Convert the camera's rotation to a forward direction vector.
# This vector indicates the direction the camera is facing.
cameraDirection = cameraRotation.get_forward_vector()

# Define a distance from the camera where the new object will be spawned.
distance = 500

# Calculate the spawn location for the new actor based on the camera's direction and the specified distance.
spawnLocation = cameraLocation + cameraDirection * distance

# Load a Blueprint asset from the specified path in the Unreal project. In this case, 'BP_Checkpoint'.
blueprint = unreal.EditorAssetLibrary.load_asset('/Game/Blueprints/BP_Checkpoint')

# Get the class from the Blueprint asset. This class is used to spawn the actor.
blueprint_class = unreal.load_class(None, blueprint.get_path_name())

# Spawn an actor of the Blueprint class at the calculated spawn location in the editor world.
new_checkpoint = unreal.EditorLevelLibrary.spawn_actor_from_object(blueprint, spawnLocation)

# Print the name of the spawned actor to the Output Log
print(f'Spawned actor with name: {new_checkpoint.get_name()}')
