# Generated by Django 3.0 on 2020-04-26 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0003_auto_20200417_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circleitem',
            name='type',
        ),
    ]
