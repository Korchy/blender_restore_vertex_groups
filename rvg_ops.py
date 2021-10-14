# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_restore_vertex_groups

from bpy.types import Operator
from bpy.utils import register_class, unregister_class
from .rvg import RVG


class RVG_OT_restore_vertex_groups(Operator):
    bl_idname = 'rvg.restore_vertex_groups'
    bl_label = 'Restore Vertex Groups'
    bl_description = 'Restore vertex groups for meshes appended from 3.0'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        RVG.restore_vertex_groups(
            context=context,
            selection=context.selected_objects
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects


def register():
    register_class(RVG_OT_restore_vertex_groups)


def unregister():
    unregister_class(RVG_OT_restore_vertex_groups)
