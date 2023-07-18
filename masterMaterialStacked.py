import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary


#Creates the master material in the specified folder within the UE5 project
masterMaterial = AssetTools.create_asset("M_MasterStacked", "/Game/Materials/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Parameter, Connect to Base Color pin of Output
baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, -300)
baseColorTextureParam.set_editor_property("Parameter_Name", "Color")
MaterialEditLibrary.connect_material_property(baseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create Constant Value for Specular, Connect to Specular pin of Output
specularParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -384, 0)
specularParam.set_editor_property("Parameter_Name", "Specular Intensity")
MaterialEditLibrary.connect_material_property(specularParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Parameter, Connect to Normal pin of Output
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, 300)
normalTextureParam.set_editor_property("Parameter_Name", "Normal")
MaterialEditLibrary.connect_material_property(normalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Creates 'Stacked' 2D Texture Parameter, Connect to ORM pins of Output
ormTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, 600)
ormTextureParam.set_editor_property("Parameter_Name", "ORM")
MaterialEditLibrary.connect_material_property(ormTextureParam, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(ormTextureParam, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(ormTextureParam, "B", unreal.MaterialProperty.MP_METALLIC)

#Create On/Off Switch for Emissive Color and Connect to Emissive Color Output
switchOnOff = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionStaticSwitchParameter, -500, 300)
switchOnOff.set_editor_property("Parameter_Name", "On/Off")
MaterialEditLibrary.connect_material_property(switchOnOff, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)

#Create a Constant at 0 that Activates when Switch is Off. Connect to False of Switch
offParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionConstant, -700, 400)
MaterialEditLibrary.connect_material_expressions(offParam, "", switchOnOff, "False")

#Create a Vector Parameter and Scalar Parameter that are Combined using a Multiply Node and Connect to True of Switch
multiplyNode = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionMultiply, -700, 150)
MaterialEditLibrary.connect_material_expressions(multiplyNode, "", switchOnOff, "True")

emissiveColorParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionVectorParameter, -900, 0)
emissiveColorParam.set_editor_property("Parameter_Name", "Emissive Color")
emissiveColorParam.set_editor_property("Default_Value", (1.0, 1.0, 1.0, 1.0))
MaterialEditLibrary.connect_material_expressions(emissiveColorParam, "", multiplyNode, "A")

emissiveIntensityParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -900, 250)
emissiveIntensityParam.set_editor_property("Parameter_Name", "Emissive Intensity")
emissiveIntensityParam.set_editor_property("Default_Value", 1.0)
MaterialEditLibrary.connect_material_expressions(emissiveIntensityParam, "", multiplyNode, "B")

#Create Material Instance
stackedMaterialInstance = AssetTools.create_asset("MI_MasterStacked", "/Game/Materials/MasterMaterials/MaterialInstances", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())

#Save Materials
EditorAssetLibrary.save_asset("/Game/Materials/MasterMaterials/M_MasterStacked", True)
EditorAssetLibrary.save_asset("/Game/Materials/MasterMaterials/MaterialInstances/MI_MasterStacked", True)