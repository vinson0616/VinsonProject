# Generated by Django 3.0 on 2020-04-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0004_remove_circleitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circleitem',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon/', verbose_name='图标'),
        ),
    ]
