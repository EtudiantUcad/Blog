# Generated by Django 4.0 on 2022-08-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0022_alter_comment_email_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='commentprofile'),
        ),
    ]
