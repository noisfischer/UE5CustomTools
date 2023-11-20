
import unreal

# Retrieve an instance of the AssetTools class. Provides functions for asset creation, duplication, etc.
AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
# Access the MaterialEditingLibrary. Provides functions to edit materials and material instances.
MaterialEditLibrary = unreal.MaterialEditingLibrary
# Access the EditorAssetLibrary. Provides functions like loading, saving and modifying assets.
EditorAssetLibrary = unreal.EditorAssetLibrary

#Creates the master material in the specified folder within the UE5 project
masterMaterial = AssetTools.create_asset("M_Master", "/Game/Materials/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Parameter, Connect to Base Color pin of Output
baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, -900)
baseColorTextureParam.set_editor_property("Parameter_Name", "Color")
MaterialEditLibrary.connect_material_property(baseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create 2D Texture Parameter, Connect to Roughness pin of Output
roughnessTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, -100)
roughnessTextureParam.set_editor_property("Parameter_Name", "Roughness")
MaterialEditLibrary.connect_material_property(roughnessTextureParam, "RGB", unreal.MaterialProperty.MP_ROUGHNESS)

#Create 2D Texture Parameter, Connect to Metallic pin of Output
metallicTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, -600)
metallicTextureParam.set_editor_property("Parameter_Name", "Metallic")
MaterialEditLibrary.connect_material_property(metallicTextureParam, "RGB", unreal.MaterialProperty.MP_METALLIC)

#Create Constant Value for Specular, Connect to Specular pin of Output
specularParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -500, -300)
specularParam.set_editor_property("Parameter_Name", "Specular Intensity")
specularParam.set_editor_property("Default_Value", 0.5)
MaterialEditLibrary.connect_material_property(specularParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Parameter, Connect to Normal pin of Output
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, 500)
normalTextureParam.set_editor_property("Parameter_Name", "Normal")
MaterialEditLibrary.connect_material_property(normalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Parameter, Connect to AO pin of Output
aoTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -500, 800)
aoTextureParam.set_editor_property("Parameter_Name", "AO")
MaterialEditLibrary.connect_material_property(aoTextureParam, "RGB", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

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

#Save Material
EditorAssetLibrary.save_asset("/Game/Materials/MasterMaterials/M_Master", True)