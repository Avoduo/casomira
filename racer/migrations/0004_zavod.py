# Generated by Django 5.0.3 on 2024-06-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racer', '0003_alter_racer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zavod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.IntegerField(null=True)),
                ('info', models.CharField(default='', max_length=3000)),
            ],
        ),
    ]
