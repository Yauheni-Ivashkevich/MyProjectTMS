# Generated by Django 3.0.7 on 2020-06-12 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_likes', models.IntegerField(blank=True, null=True)),
                ('nr_dislikes', models.IntegerField(blank=True, null=True)),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('nr_likes', models.IntegerField(blank=True, null=True)),
                ('nr_dislikes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FeedbackPost',
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='feedback.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feedback.Post'),
        ),
    ]
