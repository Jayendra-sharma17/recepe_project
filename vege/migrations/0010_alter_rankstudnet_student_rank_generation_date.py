# Generated by Django 4.2.10 on 2024-02-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_alter_rankstudnet_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankstudnet',
            name='student_rank_generation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
