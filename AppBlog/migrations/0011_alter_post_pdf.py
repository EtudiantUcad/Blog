# Generated by Django 4.1 on 2022-08-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0010_remove_post_video_post_pdf_alter_post_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pdf',
            field=models.FileField(blank=True, help_text='pdf', null=True, upload_to='document'),
        ),
    ]
