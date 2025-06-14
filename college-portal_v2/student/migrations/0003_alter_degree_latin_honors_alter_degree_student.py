# Generated by Django 5.2.1 on 2025-06-04 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='latin_honors',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='degree',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degree', to='student.student'),
        ),
    ]
