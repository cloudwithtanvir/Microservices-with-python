# Generated by Django 3.2.7 on 2021-11-08 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_comment_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]