import bpy
from pathlib import Path
import os

bl_info = {
    "name": "Import and save custom primitives",
    "author": "Flor Guilini",
    "version": (0, 2),
    "blender": (2, 79, 0),
    "location": "Add menu -> Mesh -> custom primitives",
    "description": "save and append your own primitives",
    "warning": "I don't know what the heck I'm doing",
    "wiki_url": "https://github.com/Fl0GUI/blender-scripts",
    "tracker_url": "",
    "category": "Import-Export",
    }


class append_model(bpy.types.Operator):
    bl_idname = "object.appendprimitive"
    bl_label = "append primitive"
    bl_options = {'REGISTER', 'UNDO'}
    
    object = bpy.props.StringProperty(name="import_object")
    file = bpy.props.StringProperty(name="import_file")
    
    def execute(self, context):
        return bpy.ops.wm.append(
            directory=self.file + "\\Object\\",
            filename=self.object
        )

class save_model(bpy.types.Operator):
    bl_idname = "object.saveprimitive"
    bl_label = "save to primitive"
    bl_options = {'REGISTER', 'UNDO'}

    file = bpy.props.StringProperty(name="export_file")

    def execute(self, context):
        selected = set(context.selected_objects)
        for obj in selected:
            obj.location = (0,0,0)

        bpy.data.libraries.write(
            filepath=self.file,
            datablocks=selected,
            fake_user=True
        )
        return {'FINISHED'}
            


class INFO_MT_mesh_append_add(bpy.types.Menu):
    bl_idname = "INFO_MT_mesh_append_add"
    bl_label = "add mesh"
    
    def draw(self, context):

        layout = self.layout
        layout.separator()
        
        script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
        blendfile = [str(f) for f in (script_directory.glob("*.blend"))]
        with bpy.data.libraries.load(blendfile[0]) as (blend_from, blend_to):
            for obj in blend_from.objects:
                props = layout.operator("object.appendprimitive", text=obj)
                props.file = blendfile[0]
                props.object = obj
        layout.separator()
        props = layout.operator("object.saveprimitive", text="save selected")
        props.file = blendfile[0]

        

def menufunc(self, context):
    layout = self.layout
    layout.separator()
    layout.menu("INFO_MT_mesh_append_add", text="custom primitives")
    

def register():
    bpy.utils.register_class(append_model)
    bpy.utils.register_class(save_model)
    bpy.utils.register_class(INFO_MT_mesh_append_add)
    bpy.types.INFO_MT_mesh_add.append(menufunc)

def unregister():
    bpy.utils.unregister_class(save_model)
    bpy.utils.unregister_class(append_model)
    bpy.utils.unregister_class(INFO_MT_mesh_append_add)
    bpy.types.INFO_MT_mesh_add.remove(menufunc)

if __name__ == "__main__":
    register()
