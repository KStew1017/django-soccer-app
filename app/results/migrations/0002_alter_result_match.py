# Generated by Django 3.2.2 on 2023-03-17 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='match',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='matches.match'),
        ),
    ]
