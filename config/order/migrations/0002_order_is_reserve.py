# Generated by Django 4.0.5 on 2022-06-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_reserve',
            field=models.BooleanField(default=True),
        ),
    ]