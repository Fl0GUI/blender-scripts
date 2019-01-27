import time
import bpy
from bpy import context as context
from bpy import ops as operations
bl_info= { "name": "bulk blend from shape",
           "category": "Object" }
           
class BulkBlendFromShape(bpy.types.Operator):
    """Taking VR_smoothie's job script by script"""  # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.bulkblendfromshape"          # unique identifier for buttons and menu items to reference.
    bl_label = "Bulk Blend From Shape"               # display name in the interface.
    bl_options = {'REGISTER'}                        # enable undo for the operator.

    def execute(self, context):
        
        # Check if the user is in edit mode
        if not context.mode == 'EDIT_MESH':
            self.report({'WARNING'}, "Must be in edit mode.")
            return {'CANCELLED'}
        
        object = context.active_object # get the active object
        
        # check type of active object
        if not object.type == 'MESH':
            self.report({'WARNING'}, "This object is not a mesh.")
            return {'CANCELLED'}
        
        shape_keys = object.data.shape_keys
        if not shape_keys:
            self.report({'WARNING'}, "No shape keys found, sorry.")
            return {'CANCELLED'}
            
        nsuccesful = 0 # number of succesful blend_from_shape calls
        nshapekeys = len(shape_keys.key_blocks.items()) # get number of shape keys
        OGKeyFrame = object.active_shape_key_index # get current Shape Key

        tic = time.time()
        for i in range(nshapekeys): # iterate over shape keys
            object.active_shape_key_index = i # set the active shape key
            if {'FINISHED'} == operations.mesh.blend_from_shape(add=False): # function that has to be done repetively
                nsuccesful += 1 # Count how many operations were succesful
        toc = time.time()
        
        object.active_shape_key_index = OGKeyFrame # set key frame back to original
        if nsuccesful == nshapekeys:
            self.report({'INFO'}, "Blend From Shape was succesful for all shape keys in {:.2f}s.".format(toc - tic))
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "failed {} Blend From Shape operations, sorry. ".format(nshapekeys - nsuccesful))
            return {'FINISHED'}


def register():
    bpy.utils.register_class(BulkBlendFromShape)
    
def unregister():
    bpy.utils.unregister_class(BulkBlendFromShape)

if __name__== "__main__":
     register()
