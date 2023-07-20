import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

#Creates the master material in the specified folder within the UE5 project
masterMaterial = AssetTools.create_asset("M_Glass", "/Game/Materials/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Editable Base Color
colorParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionVectorParameter, -900, 0)
colorParam.set_editor_property("Parameter_Name", "Base Color")
colorParam.set_editor_property("Default_Value", (1.0, 1.0, 1.0, 1.0))
MaterialEditLibrary.connect_material_property(colorParam, "",unreal.MaterialProperty.MP_BASE_COLOR)

#Create Scalar Parameter for Specular, Connect to Specular pin of Output
specularParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -500, -300)
specularParam.set_editor_property("Parameter_Name", "Specular")
specularParam.set_editor_property("Default_Value", 10)
MaterialEditLibrary.connect_material_property(specularParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create Scalar Parameter for Roughness
roughnessParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -500, -300)
roughnessParam.set_editor_property("Parameter_Name", "Roughness")
roughnessParam.set_editor_property("Default_Value", 0)
MaterialEditLibrary.connect_material_property(roughnessParam, "", unreal.MaterialProperty.MP_ROUGHNESS)

#Create Scalar Parameter for Opacity
opacityParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -500, -300)
opacityParam.set_editor_property("Parameter_Name", "Opacity")
opacityParam.set_editor_property("Default_Value", .5)
MaterialEditLibrary.connect_material_property(opacityParam, "", unreal.MaterialProperty.MP_OPACITY)

#Create Lerp Node
lerpNode = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionLinearInterpolate, -500, -600)
MaterialEditLibrary.connect_material_property(lerpNode, "", unreal.MaterialProperty.MP_REFRACTION)

#Create a constant value
constantNode = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionConstant, -500, -700)
MaterialEditLibrary.connect_material_expressions(constantNode, "", lerpNode, "A")

#Create Scalar Parameter for Refraction
refractionParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -500, -800)
refractionParam.set_editor_property("Parameter_Name", "Roughness Intensity")
refractionParam.set_editor_property("Default_Value", 1.4)
MaterialEditLibrary.connect_material_expressions(refractionParam, "", lerpNode, "B")

#Create Fresnel Node
fresnel = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionFresnel, -500, -1000)
MaterialEditLibrary.connect_material_expressions(fresnel, "", lerpNode, "Alpha")

#Create Scalar Parameter for Fresnel Falloff
fresnelFalloffParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionScalarParameter, -500, -1200)
fresnelFalloffParam.set_editor_property("Parameter_Name", "Fresnel Falloff")
fresnelFalloffParam.set_editor_property("Default_Value", 10)
MaterialEditLibrary.connect_material_property(fresnelFalloffParam, "", fresnel, "")

#Save Material
EditorAssetLibrary.save_asset("/Game/Materials/MasterMaterials/M_Glass", True)

print("Change material blend mode to Translucent and Lighting Mode to Surface Translucency Volume")