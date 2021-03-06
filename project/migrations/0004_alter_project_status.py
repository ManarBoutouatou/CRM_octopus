# Generated by Django 3.2 on 2022-05-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_contract_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('CO', 'confirm'), ('CP', 'completed'), ('PE', 'pending')], max_length=2, null=True),
        ),
    ]
