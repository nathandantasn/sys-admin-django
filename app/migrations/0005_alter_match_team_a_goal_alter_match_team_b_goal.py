# Generated by Django 4.2.3 on 2023-08-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_a_goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_b_goal',
            field=models.IntegerField(default=0),
        ),
    ]
