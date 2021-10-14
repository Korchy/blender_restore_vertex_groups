# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_restore_vertex_groups

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class RVG_PT_panel(Panel):
    bl_idname = 'RVG_PT_panel'
    bl_label = 'RVG'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RVG'

    def draw(self, context):
        self.layout.operator('rvg.restore_vertex_groups', icon='GROUP_VERTEX')


def register():
    register_class(RVG_PT_panel)


def unregister():
    unregister_class(RVG_PT_panel)
