import unreal

editor_util = unreal.EditorUtilityLibrary()
selected_actors = editor_util.get_selection_set()

for actor in selected_actors:
    actor.tags = []
    unreal.log("Removed all tags from actor {}".format(actor.get_name()))

unreal.log("Finished removing tags from selected actors.")