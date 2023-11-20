import unreal

levelTools = unreal.Level  # Provides access to level-related functions.
editorLevelLibrary = unreal.EditorLevelLibrary  # Provides level editing functionalities.
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)  # Accesses the level editor subsystem.

# Define the name for a new level.
newLevel = "myNewLevel"

# Create a new level using the Level Editor Subsystem. The new level is created in the "/Game/Levels" directory.
myNewLevel = levelSubSys.new_level("/Game/Levels/newLevel")

# Open the newly created level
levelSubSys.set_current_level_by_name(newLevel)

# Save the new level
levelSubSys.save_current_level()
