# Generated by Django 4.2.10 on 2024-02-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0010_alter_rankstudnet_student_rank_generation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_rank',
            field=models.IntegerField(default=200),
        ),
    ]