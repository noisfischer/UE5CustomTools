import unreal

# Set the location for the new floor actor at center of level
location = unreal.Vector(0.0, 0.0, 0.0)  # X, Y, Z coordinates

# Set the rotation for the new floor
rotation = unreal.Rotator(0.0, 0.0, 0.0)  # Pitch, Yaw, Roll

# Set the scale for the new floor
scale = unreal.Vector(100.0, 100.0, 1.0)  # Scale in X, Y, Z directions

# Create a new Actor with StaticMeshComponent (in this case, a floor)
new_floor = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.StaticMeshActor, location, rotation)

# Get the Static Mesh Component from the newly created Actor
static_mesh_component = new_floor.get_component_by_class(unreal.StaticMeshComponent)

# Set the Static Mesh for the new floor (here, a simple plane is used)
# You can replace '/Engine/BasicShapes/Plane' with your own asset path if you have a custom floor design
asset_path = "/Engine/BasicShapes/Cube"
static_mesh = unreal.load_object(None, asset_path)

# Assign the mesh to the StaticMeshComponent
static_mesh_component.set_static_mesh(static_mesh)

# Set the scale for the StaticMeshComponent
static_mesh_component.set_world_scale3d(scale)

print("Successfully spawned a new floor in the center of the level.")
