# Generated by Django 2.0.4 on 2018-04-16 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_pokemon_base_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
