import bpy
bl_info= { "name": "bulk blend from shape",
           "category": "Object" }
           
class BulkBlendFromShape(bpy.types.Operator):
    """Taking VR_smoothie's job script by script"""  # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.bulkblendfromshape"          # unique identifier for buttons and menu items to reference.
    bl_label = "Bulk Blend From Shape"               # display name in the interface.
    bl_options = {'REGISTER'}                        # enable undo for the operator.

    def execute(self, context):
        object = bpy.context.active_object # get the active object
        nshapekeys = len(bpy.context.object.data.shape_keys.key_blocks.items()) # get number of shape keys
        OGKeyFrame = bpy.context.active_object.active_shape_key_index # get current Shape Key
        for i in range(nshapekeys): # iterate over shape keys
            object.active_shape_key_index = i # set the active shape key
            bpy.ops.mesh.blend_from_shape(add=False) # function that has to be done repetively
        object.active_shape_key_index = OGKeyFrame # set key frame back to original
        return {'FINISHED'}

def register():
    bpy.utils.register_class(BulkBlendFromShape)
    
def unregister():
    bpy.utils.unregister_class(BulkBlendFromShape)

if __name__== "__main__":
     register()
