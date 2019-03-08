# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-09 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(db_column='semail', max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], db_column='ssex', default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (1, '通过'), (2, '拒绝')], db_column='sstatus', default=0, verbose_name='审核状态'),
        ),
    ]
