# Generated by Django 5.0.3 on 2024-06-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racer', '0010_remove_racer_choice_field_alter_racer_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racer',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='racer',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
    ]
