# Generated by Django 4.1.5 on 2023-01-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.CharField(max_length=255)),
                ('Titel', models.CharField(max_length=255)),
                ('beschreibnung', models.CharField(max_length=255)),
                ('Ansprechpartner', models.CharField(max_length=255)),
            ],
        ),
    ]
