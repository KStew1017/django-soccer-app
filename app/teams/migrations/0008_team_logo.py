# Generated by Django 3.2.2 on 2023-03-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_alter_team_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
