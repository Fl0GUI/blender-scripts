import bpy

bl_info = {
    "name": "remove all doubles",
    "description": "removes the doubles from all meshes, use in object mode",
    "author": "me :)",
    "blender": (2,80,0),
    "location": "F3 menu",
    "warning": "No clue what I am doing",
    "category": "Mesh"
    }

class RemoveDoublesFromAll(bpy.types.Operator):
    bl_idname = "object.removedoublesfromall"
    bl_label = "remove all doubles"
    bl_options = {'REGISTER'}

    def execute(self, context):
        for obj in bpy.data.objects:
            context.view_layer.objects.active = obj
            if bpy.ops.object.editmode_toggle.poll(): 
                bpy.ops.object.editmode_toggle()
            if bpy.ops.mesh.select_all.poll():
                bpy.ops.mesh.select_all(action='SELECT')
            if bpy.ops.mesh.remove_doubles.poll():
                bpy.ops.mesh.remove_doubles(use_unselected=True)
            if bpy.ops.object.editmode_toggle.poll(): 
                bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RemoveDoublesFromAll)
def unregister():
    bpy.utils.unregister_class(RemoveDoublesFromAll)
