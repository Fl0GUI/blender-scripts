import bpy
bl_info= { "name": "remove all shape keys",
           "category": "Object" }
           
class RemoveAllShapeKeys(bpy.types.Operator):
    """Taking VR_smoothie's job script by script"""  # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.removeallshapekeys"          # unique identifier for buttons and menu items to reference.
    bl_label = "Remove All Shape Keys"               # display name in the interface.
    bl_options = {'REGISTER'}                        # enable undo for the operator.

    def execute(self, context):
        if bpy.context.object.data.shape_keys != None:
            bpy.ops.object.shape_key_remove(all=True)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RemoveAllShapeKeys)
    
def unregister():
    bpy.utils.unregister_class(RemoveAllShapeKeys)

#bpy.ops.object.shape_key_remove(all=True)

if __name__== "__main__":
     register()