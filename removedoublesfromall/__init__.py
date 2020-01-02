import bpy

bl_info = {
    "name": "remove all the doubles",
    "description": "removes doubles from all meshes",
    "author": "Flor Guilini",
    "version": (420, 69),
    "blender": (2,80,0),
    "location": "Object",
    "warning": "I don't know what the heck I'm doing",
    "wiki_url": "https://github.com/Fl0GUI/blender-scripts",
    "tracker_url": "",
    "category": "Object"
}

class RemoveDoublesFromAll(bpy.types.Operator):
    bl_idname = "object.removedoublesfromall"
    bl_label = "remove all doubles"
    bl_options = {'REGISTER'}

    def execute(self, context):
        for obj in bpy.data.objects:
            context.scene.objects.active = obj
            if bpy.ops.object.editmode_toggle.poll(): 
                bpy.ops.object.editmode_toggle()
            if bpy.ops.mesh.select_all.poll():
                bpy.ops.mesh.select_all(action='SELECT')
            if bpy.ops.mesh.remove_doubles.poll():
                bpy.ops.mesh.remove_doubles(use_unselected=True)
            if bpy.ops.object.editmode_toggle.poll(): 
                bpy.ops.object.editmode_toggle()
        return {'FINISHED'}

def addUI(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("object.removedoublesfromall", text="remove doubles from all meshes")

def register():
    bpy.utils.register_class(RemoveDoublesFromAll)
    bpy.types.VIEW3D_MT_object.append(addUI)
def unregister():
    bpy.utils.unregister_class(RemoveDoublesFromAll)
    bpy.types.VIEW3D_MT_object.remove(addUI)
