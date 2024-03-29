# Generated by Django 3.2 on 2022-08-03 08:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, editable=False, populate_from='get_unicode_words', unique=True),
        ),
    ]
