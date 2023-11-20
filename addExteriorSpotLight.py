
import unreal

#Create light actor
spotLight = unreal.SpotLight

#Get the editor viewport client
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
viewport = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()

cameraLocation = viewport[0]
cameraRotation = viewport[1]

#Converts the rotation to a direction vector
cameraDirection = cameraRotation.get_forward_vector()

#Specifies distance from camera at which to spawn the spot light
distance = 500

#Calculates spawn location
spawnLocation = cameraLocation + cameraDirection * distance

#Spawn the actor
newSpotLightActor = unreal.EditorLevelLibrary.spawn_actor_from_class(spotLight, spawnLocation)

#Set the rotation of the spot light to aim straight down
newSpotLightActor.set_actor_rotation(unreal.Rotator(0.0, -90.0, 0.0), True)

#Get light component
lightComponent = newSpotLightActor.spot_light_component

#Set light settings
lightComponent.set_editor_property('inner_cone_angle', 20.0)
lightComponent.set_editor_property('outer_cone_angle', 45.0)
lightComponent.set_editor_property('attenuation_radius', 500)
lightComponent.set_editor_property('intensity', 50)
lightComponent.set_editor_property('use_temperature', True)
lightComponent.set_editor_property('temperature', 5600)

# #Save changes
# levelSubSys.save_current_level()