# Generated by Django 3.0 on 2020-08-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20200826_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='type',
            field=models.IntegerField(choices=[(0, '自考'), (1, '成教'), (2, '国开')], default=0, verbose_name='报考类型'),
        ),
    ]