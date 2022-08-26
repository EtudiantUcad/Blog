# Generated by Django 4.0 on 2022-08-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0019_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Email_documents/'),
        ),
        migrations.AlterField(
            model_name='email',
            name='message',
            field=models.TextField(max_length=10000),
        ),
    ]