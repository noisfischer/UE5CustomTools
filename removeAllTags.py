import unreal

# Create instance of EditorUtilityLibrary. Provides functions for interacting with UE editor
editor_util = unreal.EditorUtilityLibrary()

# Retrieve list of currently selected actors in UE editor.
selected_actors = editor_util.get_selection_set()

# Iterate through each actor in the list of selected actors.
for actor in selected_actors:
    # Clear the tags list of the actor. This removes all tags that have been assigned to the actor.
    actor.tags = []
    # Log a message to Output Log for each actor, indicating that all tags have been removed.
    unreal.log("Removed all tags from actor {}".format(actor.get_name()))

# Once loop is complete, log a final message that indicates completion of task
unreal.log("Finished removing tags from selected actors.")
