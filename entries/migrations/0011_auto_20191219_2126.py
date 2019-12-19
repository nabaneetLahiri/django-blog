# Generated by Django 2.0.8 on 2019-12-19 15:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0010_entry_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='slug',
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
