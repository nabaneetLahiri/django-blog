# Generated by Django 2.2.1 on 2019-12-12 08:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20191207_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
