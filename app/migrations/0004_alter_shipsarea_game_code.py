# Generated by Django 4.0.2 on 2022-02-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_shipsarea_game_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipsarea',
            name='game_code',
            field=models.IntegerField(blank=True, null=True, unique=2),
        ),
    ]
