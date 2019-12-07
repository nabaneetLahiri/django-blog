# Generated by Django 2.2.1 on 2019-12-07 12:12

from django.db import migrations, models
import entries.models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=entries.models.upload_location),
        ),
    ]
