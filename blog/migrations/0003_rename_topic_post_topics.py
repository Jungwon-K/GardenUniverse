# Generated by Django 5.2 on 2025-04-11 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='topic',
            new_name='topics',
        ),
    ]
