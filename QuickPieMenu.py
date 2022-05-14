bl_info = {
    "name" : "QuickPie",
    "author" : "neilius maximus",
    "version" : ( 1, 0),
    "blender" : ( 2, 81, 0),
    "location" : "View3D ",
    "warning" : "may have some bugs",
    "wiki_url" : "www.blender.org",
    "description": "Making something easy",
    "category" : "General Tools for personal Use"}

 
import bpy
from bpy.types import Menu

#rename and reuse all of this
class VIEW_3D_MT_PIE(Menu):
    bl_label = "localGlobalPie" # text on panels side bar
    bl_idname = "quick.pie"
    
    def draw(self, context):
        layout = self.layout
        
        pie = layout.menu_pie() # row can be used to create new lines
        #row.label(text = "Animations") ## this is how you add textt
        #row = layout.row() # row can be used to create new lines
        #row.operator("mesh.primitive_plane_add") ## adding objects using operator
        #row.operator("transform.transl
        #pie.operator_enum("mesh.select_mode", "type")
        pie.operator("quick.global")
        pie.operator("quick.local")
        pie.operator("quick.mov")
        pie.operator("quick.rot")
        pie.operator("quick.keyrot")
        pie.operator("quick.keyloc")
        pie.operator("quick.play")
        pie.operator("quick.back")
        #pie.operator("context.space_data.overlay.show_overlays = True")
        #pie.operator(
        #pie.operator_enum("ops.wm.tool_set_by_id","name")
        #
        

class QuickGlobal(bpy.types.Operator):
    bl_label = "Global"
    bl_idname = "quick.global"
    
    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'
        return {'FINISHED'}

class QuickRot(bpy.types.Operator):
    bl_label = "Rot"
    bl_idname = "quick.rot"
    
    def execute(self, context):
        bpy.ops.wm.tool_set_by_index(index=6)
        return {'FINISHED'}
    
class QuickMov(bpy.types.Operator):
    bl_label = "Move"
    bl_idname = "quick.mov"
    
    def execute(self, context):
        bpy.ops.wm.tool_set_by_index(index=5)
        return {'FINISHED'}

class QuickLocal(bpy.types.Operator):
    bl_label = "Local"
    bl_idname = "quick.local"
    
    def execute(self, context):
        bpy.context.scene.transform_orientation_slots[0].type = 'LOCAL'
        return {'FINISHED'}
    
class QuickKeyRot(bpy.types.Operator):
    bl_label = "KeyRot"
    bl_idname = "quick.keyrot"
    
    def execute(self, context):
        bpy.ops.anim.keyframe_insert_menu(type = 'Rotation')
        return {'FINISHED'}
    
class QuickKeyLoc(bpy.types.Operator):
    bl_label = "KeyLoc"
    bl_idname = "quick.keyloc"
    
    def execute(self, context):
        bpy.ops.anim.keyframe_insert_menu(type = 'Location')
        return {'FINISHED'}
    
class QuickPlay(bpy.types.Operator):
    bl_label = "Play"
    bl_idname = "quick.play"
    
    def execute(self, context):
        bpy.ops.screen.animation_play()
        return {'FINISHED'}
    
class QuickBack(bpy.types.Operator):
    bl_label = "Back"
    bl_idname = "quick.back"
    
    def execute(self, context):
        bpy.ops.screen.keyframe_jump(next = False)
        return {'FINISHED'}

classes = [QuickBack,QuickPlay,VIEW_3D_MT_PIE,QuickGlobal,QuickLocal,QuickMov,QuickRot,QuickKeyLoc,QuickKeyRot]  
     
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
        
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    
if __name__ == "__main__":
    register()
    bpy.ops.wm.call_menu_pie(name="VIEW_3D_MT_PIE")
    
    