import bpy

for obj in bpy.data.objects:
    bpy.context.scene.objects.active = obj
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.object.editmode_toggle()