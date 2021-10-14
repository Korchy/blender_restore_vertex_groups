# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_restore_vertex_groups

class RVG:

    @classmethod
    def restore_vertex_groups(cls, context, selection):
        # restore vertex groups
        objects = (obj for obj in selection if obj.type == 'MESH')
        for obj in objects:
            # find max group count for each vertices
            max_groups_count = max([len(v.groups) for v in obj.data.vertices])
            # create groups for each object
            # groups id's are already saved in vertex.groups
            # so when create group - data connects to it automatically
            existed_groups_count = len(obj.vertex_groups)
            if max_groups_count > existed_groups_count:
                for i in range(max_groups_count - existed_groups_count):
                    obj.vertex_groups.new()
