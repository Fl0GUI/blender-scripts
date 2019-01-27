import bpy
from bpy import context
bl_info= { "name": "remove all shape keys",
           "category": "Object" }
           
class RemoveAllShapeKeys(bpy.types.Operator):
    """Taking VR_smoothie's job script by script"""  # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.removeallshapekeys"          # unique identifier for buttons and menu items to reference.
    bl_label = "Remove All Shape Keys"               # display name in the interface.
    bl_options = {'REGISTER'}                        # enable undo for the operator.

    def execute(self, context):
        
        # Check if the user is in edit mode
        if not context.mode == 'OBJECT':
            self.report({'WARNING'}, "Must be in Object Mode.")
            return {'CANCELLED'}
        
        object = context.active_object # selected object
        
        # check the type of the active object
        if not object.type == 'MESH':
            self.report({'WARNING'}, "This object is not a mesh.")
            return {'CANCELLED'}
            
        if object.data.shape_keys: # remove all shape keys if present
            nshapekeys = len(object.data.shape_keys.key_blocks)
            bpy.ops.object.shape_key_remove(all=True)
            self.report({'INFO'}, "Removed {} Shape Keys.".format(nshapekeys))
        else:
            self.report({'WARNING'}, "No Shape Keys to remove.")
            
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RemoveAllShapeKeys)
    
def unregister():
    bpy.utils.unregister_class(RemoveAllShapeKeys)

#bpy.ops.object.shape_key_remove(all=True)

if __name__== "__main__":
     register()