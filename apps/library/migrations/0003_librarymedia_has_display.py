# Generated by Django 3.0 on 2020-05-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200503_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarymedia',
            name='has_display',
            field=models.BooleanField(default=False, verbose_name='首页显示'),
        ),
    ]