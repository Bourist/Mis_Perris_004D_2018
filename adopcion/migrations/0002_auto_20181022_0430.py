# Generated by Django 2.1.2 on 2018-10-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='fono',
            field=models.CharField(max_length=8),
        ),
    ]
