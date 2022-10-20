import bpy
from . import mb_server


def update_sphere_size(properties_group, context):
    sphere_size = properties_group.sphere_size
    if mb_server.mastodon_blender_server is not None:
        mb_server.mastodon_blender_server.many_spheres.set_sphere_size(
            sphere_size)


class BlenderMastodonViewProperties(bpy.types.PropertyGroup):
    sphere_size: bpy.props.FloatProperty(name="Sphere Size", soft_min=0.05,
                                         soft_max=1.0, default=0.1,
                                         update=update_sphere_size)


class TestPanel(bpy.types.Panel):
    bl_label = "Mastodon 3D View"
    bl_idname = "_PT_ Mastodon 3D View"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mastodon 3D View'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.blender_mastodon_view_properties,
                    "sphere_size")
        row = layout.row()
        row.label(text="gRPC Hello World Example 3", icon='CUBE')


classes = [TestPanel, BlenderMastodonViewProperties]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.blender_mastodon_view_properties = \
        bpy.props.PointerProperty(type=BlenderMastodonViewProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.blender_mastodon_view_properties


if __name__ == "__main__":
    register()
