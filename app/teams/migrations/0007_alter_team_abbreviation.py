# Generated by Django 3.2.2 on 2023-03-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20230323_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='abbreviation',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]