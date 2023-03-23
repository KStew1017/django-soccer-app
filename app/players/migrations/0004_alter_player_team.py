# Generated by Django 3.2.2 on 2023-03-23 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_alter_team_abbreviation'),
        ('players', '0003_alter_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(db_column='team', on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
