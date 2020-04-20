# Generated by Django 3.0 on 2020-04-17 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0002_auto_20200417_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('image', models.ImageField(blank=True, null=True, upload_to='company-history/', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '公司历史',
                'verbose_name_plural': '公司历史',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='公司名称'),
        ),
    ]