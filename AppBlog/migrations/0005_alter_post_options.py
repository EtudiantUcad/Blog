# Generated by Django 4.1 on 2022-08-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_alter_post_categorie_alter_post_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['datetime']},
        ),
    ]
