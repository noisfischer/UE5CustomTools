import unreal

# Get the Editor Utility Library, which contains functions for interacting with the editor
editor_util = unreal.EditorUtilityLibrary()

# Get the currently selected actors in the editor viewport
selected_actors = editor_util.get_selection_set()

# Loop through the list of selected actors and add a tag to each one
for actor in selected_actors:
    # Get the existing list of tags from the actor
    existing_tags = actor.tags

    # Define the new tag
    new_tag = unreal.Name("WallRun")

    # Check if the actor already has the new tag
    if new_tag not in existing_tags:
        # Add the new tag to the actor's list of tags
        existing_tags.append(new_tag)
        unreal.log("Added tag {} to actor {}".format(new_tag, actor.get_name()))

# Notify that the script is done
unreal.log("Finished adding tags to selected actors.")
