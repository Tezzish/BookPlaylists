# Generated by Django 4.1 on 2022-08-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_name', models.CharField(max_length=255)),
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_authorName', models.CharField(max_length=255)),
            ],
        ),
    ]
