# Generated by Django 3.0.7 on 2020-06-22 13:24

from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20200612_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=''),
        ),
    ]
