# Generated by Django 5.0.3 on 2024-06-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racer', '0005_alter_zavod_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racer',
            name='firstname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='racer',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zavod',
            name='date',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='zavod',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
