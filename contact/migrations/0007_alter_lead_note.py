# Generated by Django 3.2 on 2022-05-24 13:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_employee_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='note',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
