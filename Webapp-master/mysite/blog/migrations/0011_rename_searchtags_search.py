# Generated by Django 5.0.1 on 2024-02-11 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_tags_searchtags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SearchTags',
            new_name='Search',
        ),
    ]
