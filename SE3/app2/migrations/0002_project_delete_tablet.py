# Generated by Django 4.0.1 on 2023-01-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titel', models.CharField(max_length=255)),
                ('beschreibung', models.CharField(max_length=255)),
                ('ansprechpartner', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='tablet',
        ),
    ]
