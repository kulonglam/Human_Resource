# Generated by Django 4.2.1 on 2023-05-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0003_alter_employee_dob_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp246', max_length=70),
        ),
    ]