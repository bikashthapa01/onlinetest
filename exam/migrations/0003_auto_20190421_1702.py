# Generated by Django 2.2 on 2019-04-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exam_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='op_first',
            new_name='op_A',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='op_fourth',
            new_name='op_B',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='op_second',
            new_name='op_C',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='op_third',
            new_name='op_D',
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_op',
            field=models.CharField(choices=[('A', 'A'), ('A', 'B'), ('A', 'C'), ('D', 'D')], max_length=10),
        ),
    ]