# Generated by Django 3.1.2 on 2020-12-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_page', '0007_auto_20201204_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaries',
            name='emp_no',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='salaries',
            table='salary',
        ),
    ]