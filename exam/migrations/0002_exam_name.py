# Generated by Django 2.2 on 2019-04-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
