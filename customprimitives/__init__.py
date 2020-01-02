import bpy
from pathlib import Path
import os

bl_info= {
    "name": "Import and save custom primitives",
    "author": "Flor Guilini",
    "version": (420, 69),
    "blender": (2, 80, 0),
    "location": "Add menu -> Mesh -> custom primitives",
    "description": "save and append your own primitives",
    "warning": "I don't know what the heck I'm doing",
    "wiki_url": "https://github.com/Fl0GUI/blender-scripts",
    "tracker_url": "",
    "category": "Import-Export",
    }



class remove_model(bpy.types.Operator):
    bl_idname = "object.removeprimitive"
    bl_label = "remove primitive"

    file = bpy.props.StringProperty(name="import_file")

    def execute(self, context):
        os.remove(self.file)
        return {'FINISHED'}


class import_model(bpy.types.Operator):
    bl_idname = "object.importprimitive"
    bl_label = "append primitive"
    bl_options = {'REGISTER', 'UNDO'}
    
    object = bpy.props.StringProperty(name="import_object")
    file = bpy.props.StringProperty(name="import_file")
    
    def execute(self, context):
        bpy.ops.wm.append(
            directory=self.file + "\\Object\\",
            filename=self.object
        )
        ob = self.object
        nextob = self.object + '.001'
        dub = 2
        # find the new object
        while(nextob in bpy.data.objects):
            ob = nextob
            nextob = self.object + ".{:03d}".format(dub)
            dub += 1
        bpy.data.objects[ob].location = context.scene.cursor_location
        return {'FINISHED'}

class save_model(bpy.types.Operator):
    bl_idname = "object.saveprimitive"
    bl_label = "save to primitive"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        selected = set(context.selected_objects)
        
        script_directory = Path(os.path.dirname(os.path.abspath(__file__)))

        for ob in selected:
            bpy.data.libraries.write(
                filepath=str(script_directory / (ob.name + ".blend")),
                datablocks=selected,
                fake_user=True
            )
        return {'FINISHED'}
            
class INFO_MT_mesh_primitive_remove(bpy.types.Menu):
    bl_idname = "INFO_MT_mesh_primitive_remove"
    bl_label = "remove primitives"

    files = bpy.props.StringProperty(name="primitive_files")

    def draw(self, context):
        layout = self.layout
        layout.separator()
        script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
        blendfile = [str(f) for f in (script_directory.glob("*.blend"))]
        for obj in blendfile:
            with bpy.data.libraries.load(obj) as (blend_from, blend_to):
                props = layout.operator("object.removeprimitive", text=blend_from.objects[0])
                props.file = str(obj)

class INFO_MT_mesh_primitive_add(bpy.types.Menu):
    bl_idname = "INFO_MT_mesh_primitive_add"
    bl_label = "add mesh"
    
    def draw(self, context):

        layout = self.layout
        layout.separator()
        
        script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
        blendfile = [str(f) for f in (script_directory.glob("*.blend"))]
        if len(blendfile) > 0 :
            for obj in blendfile:
                with bpy.data.libraries.load(obj) as (blend_from, blend_to):
                    props = layout.operator("object.importprimitive", text=blend_from.objects[0])
                    props.file = obj
                    props.object = blend_from.objects[0]
            layout.separator()
        props = layout.operator("object.saveprimitive", text="Save selected")
        if len(blendfile) > 0:
            layout.separator()
            layout.menu("INFO_MT_mesh_primitive_remove")


        

def menufunc(self, context):
    layout = self.layout
    layout.separator()
    layout.menu("INFO_MT_mesh_primitive_add", text="custom primitives")
    

def register():
    print("hi")
    bpy.utils.register_class(remove_model)
    bpy.utils.register_class(import_model)
    bpy.utils.register_class(save_model)
    bpy.utils.register_class(INFO_MT_mesh_primitive_add)
    bpy.utils.register_class(INFO_MT_mesh_primitive_remove)
    bpy.types.INFO_MT_mesh_add.append(menufunc)

def unregister():
    bpy.utils.unregister_class(remove_model)
    bpy.utils.unregister_class(save_model)
    bpy.utils.unregister_class(import_model)
    bpy.utils.unregister_class(INFO_MT_mesh_primitive_add)
    bpy.utils.unregister_class(INFO_MT_mesh_primitive_remove)
    bpy.types.INFO_MT_mesh_add.remove(menufunc)

if __name__ == "__main__":
    register()
