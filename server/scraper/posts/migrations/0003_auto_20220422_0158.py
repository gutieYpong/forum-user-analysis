# Generated by Django 3.2.12 on 2022-04-21 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220421_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author_id',
            new_name='author',
        ),
    ]