# Generated by Django 5.0.3 on 2024-06-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racer', '0006_alter_racer_firstname_alter_racer_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('country', models.CharField(choices=[('US', 'United States'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy')], max_length=300)),
            ],
        ),
    ]
