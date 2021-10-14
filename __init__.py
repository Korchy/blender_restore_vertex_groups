# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_restore_vertex_groups

from . import rvg_ops
from . import rvg_ui
from .addon import Addon


bl_info = {
    'name': 'Restore Vertex Groups',
    'category': 'All',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 93, 0),
    'location': '3D Viewport window - RVG tab',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-restore-vertex-groups/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-restore-vertex-groups/',
    'description': 'Restore vertex groups in 2.9 after appending meshes from 3.0'
}


def register():
    if not Addon.dev_mode():
        rvg_ops.register()
        rvg_ui.register()
    else:
        print('It seems you are trying to use the dev version of the '
              + bl_info['name']
              + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        rvg_ui.unregister()
        rvg_ops.unregister()


if __name__ == '__main__':
    register()
