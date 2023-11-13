import unreal

# Get editor subsystems and viewport info
viewport = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()

# Get camera location and rotation
cameraLocation = viewport[0]
cameraRotation = viewport[1]

# Get camera direction
cameraDirection = cameraRotation.get_forward_vector()

# Specify distance from camera to spawn the actor
distance = 500

# Calculate spawn location
spawnLocation = cameraLocation + cameraDirection * distance

# Spawn a StaticMeshActor
new_moving_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor.static_class(), spawnLocation)

# Set its mesh
cube_mesh = unreal.EditorAssetLibrary.load_asset("/Game/StarterContent/Shapes/Shape_Cube")
new_moving_actor.static_mesh_component.set_static_mesh(cube_mesh)

# Get the actor's root component
actor_root = new_moving_actor.get_root_component()

# Create and attach a new component (Replace unreal.MyCustomComponent with your actual component's class)
new_component = unreal.ActorComponent.create_actor_component(new_moving_actor, unreal.EaseMover.static_class())
new_component.attach_to_component(actor_root, unreal.AttachmentRule.KEEP_RELATIVE, "")

# Output a success message
if new_component:
    print(f"Successfully attached {new_component.get_name()} to {new_moving_actor.get_name()}")
