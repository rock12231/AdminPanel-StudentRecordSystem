# Generated by Django 4.1.5 on 2023-01-27 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_rename_studentattandance_studentattendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentattendance',
            old_name='student_name',
            new_name='student_id',
        ),
    ]
