# Generated by Django 4.0.2 on 2022-02-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_shipsarea_game_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipsarea',
            name='game_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
