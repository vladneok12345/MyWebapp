# Generated by Django 5.0.1 on 2024-02-11 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_tags_tags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='SearchTags',
        ),
    ]
