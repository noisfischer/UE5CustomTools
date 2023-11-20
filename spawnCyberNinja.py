import unreal

# Get current level
editor_world = unreal.EditorLevelLibrary.get_editor_world()

# Get editor viewport client
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
viewport = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()

# Assign location and rotation values to variables
cameraLocation = viewport[0]
cameraRotation = viewport[1]

# Converts the rotation to a forward direction vector of camera
cameraDirection = cameraRotation.get_forward_vector()

# Specifies distance from camera at which to spawn the enemy
distance = 500

# Calculates spawn location in front of camera
spawnLocation = cameraLocation + cameraDirection * distance

# Get Blueprint class
blueprint = unreal.EditorAssetLibrary.load_asset('/Game/EnemyAI/EnemyBase/BP_EnemyBase')
blueprint_class = unreal.load_class(None, blueprint.get_path_name())

# Spawn the enemy blueprint
new_enemy_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(blueprint, spawnLocation)

# Output the name of the spawned actor
print(f'Spawned actor with name: {new_enemy_actor.get_name()}')
