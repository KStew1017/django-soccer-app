# Generated by Django 3.2.2 on 2023-03-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20230323_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='time',
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_form',
            field=models.CharField(default='TBD', max_length=5),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_record',
            field=models.CharField(default='TBD', max_length=10),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_form',
            field=models.CharField(default='TBD', max_length=5),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_record',
            field=models.CharField(default='TBD', max_length=10),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
