# Generated by Django 4.0.1 on 2023-02-13 09:16

import chat.models
import chat.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_tvdevice_remote_last_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvdevice',
            name='remote_last_image_url',
            field=models.ImageField(default='', storage=chat.storage.OverwriteStorage(), upload_to=chat.models.image_path),
            preserve_default=False,
        ),
    ]
