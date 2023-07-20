import unreal

#Create light
elevator = unreal.EditorAssetLibrary.load_blueprint_class('/Game/Blueprints/BP_Elevator')

#Get the editor viewport client
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
viewport = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()

cameraLocation = viewport[0]
cameraRotation = viewport[1]

#Converts the rotation to a direction vector
cameraDirection = cameraRotation.get_forward_vector()

#Specifies distance from camera at which to spawn the spot light
distance = 1000

#Calculates spawn location
spawnLocation = cameraLocation + cameraDirection * distance

#Spawn the actor
newElevatorBlueprintActor = unreal.EditorLevelLibrary.spawn_actor_from_class(elevator, spawnLocation)

# #Save changes
# levelSubSys.save_current_level()