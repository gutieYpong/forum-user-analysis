# Generated by Django 3.2.12 on 2022-04-21 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created'], 'verbose_name': '回覆', 'verbose_name_plural': '回覆'},
        ),
        migrations.AlterModelOptions(
            name='lihkgson',
            options={'ordering': ['lihkgson_id'], 'verbose_name': '連登仔', 'verbose_name_plural': '連登仔'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['imported'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='topic',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='lihkgson',
            old_name='id',
            new_name='lihkgson_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='author_id',
        ),
    ]
