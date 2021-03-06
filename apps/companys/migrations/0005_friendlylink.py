# Generated by Django 3.0 on 2020-04-17 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0004_auto_20200417_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendlyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='friendly/', verbose_name='图片')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
    ]
