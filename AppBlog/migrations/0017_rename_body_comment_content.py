# Generated by Django 4.0 on 2022-08-20 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0016_alter_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
    ]