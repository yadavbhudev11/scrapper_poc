# Generated by Django 2.2 on 2019-04-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_auto_20190425_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notif',
            name='publish',
            field=models.TextField(),
        ),
    ]
