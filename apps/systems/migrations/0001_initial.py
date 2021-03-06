# Generated by Django 3.0 on 2020-04-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CircleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='简述')),
                ('type', models.CharField(choices=[('big', '大'), ('small', '小')], default='大', max_length=10)),
                ('icon', models.CharField(max_length=100, verbose_name='图标')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='链接地址')),
            ],
            options={
                'verbose_name': '圆形内容',
                'verbose_name_plural': '圆形内容',
            },
        ),
    ]
