# Generated by Django 4.1 on 2022-09-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFulvito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='año_fundacion',
            field=models.IntegerField(),
        ),
    ]
