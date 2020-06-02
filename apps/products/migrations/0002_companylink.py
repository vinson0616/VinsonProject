# Generated by Django 3.0 on 2020-06-02 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品名称')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '公司环节',
                'verbose_name_plural': '公司环节',
            },
        ),
    ]