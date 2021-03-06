# Generated by Django 3.1.7 on 2021-03-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentName', models.CharField(max_length=255)),
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=100)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=50)),
            ],
        ),
    ]
