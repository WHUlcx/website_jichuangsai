# Generated by Django 2.2 on 2021-08-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data2display', '0003_remove_datapost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapost',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
