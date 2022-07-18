# Generated by Django 3.2.13 on 2022-06-15 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_emp_experince'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_designation',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]