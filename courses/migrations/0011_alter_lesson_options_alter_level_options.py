# Generated by Django 4.1.7 on 2023-03-22 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_date_alter_lesson_date_alter_level_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['date']},
        ),
    ]
