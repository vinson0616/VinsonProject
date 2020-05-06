# Generated by Django 3.0 on 2020-05-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarymedia',
            name='format',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='文件格式'),
        ),
        migrations.AddField(
            model_name='librarymedia',
            name='size',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='文件大小(MB)'),
        ),
    ]