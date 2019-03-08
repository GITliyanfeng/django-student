from django.db import models


# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, db_column='sname', verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, default=0, db_column='ssex', verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业', db_column='sprofession')
    email = models.EmailField(verbose_name='邮箱', db_column='semail')
    qq = models.CharField(max_length=128, db_column='sqq', verbose_name='QQ')
    phone = models.CharField(max_length=128, verbose_name='电话', db_column='sphone')
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='审核状态', db_column='sstatus')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间', db_index=True)

    def __str__(self):
        return f'<Student: {self.name}>'

    class Meta:
        db_table = 'student_Student'
        verbose_name = '学员信息'
        verbose_name_plural = verbose_name
