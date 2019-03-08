# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 0008 20:16
# @Author  : __Yanfeng
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from student.models import Student
import re


class BaseStudentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=20)
    sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    profession = forms.CharField(label='职业', max_length=30)
    email = forms.EmailField(label='邮箱', max_length=128)
    qq = forms.CharField(label='QQ', max_length=128)
    phone = forms.CharField(label='手机', max_length=11, min_length=11)


class StudentForm(forms.ModelForm):
    def clean_qq(self):
        qq = self.cleaned_data['qq']
        if not re.match('[0-9]{8,12}', qq):
            raise forms.ValidationError('必须是8-11位数字', code='qq invalid')
        return qq

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', phone):
            raise forms.ValidationError('手机号码格式非法', code='mobile invalid')
        return phone

    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match('[\u4e00-\u9fa5]{2,5}$', name):
            raise forms.ValidationError('只支持中文姓名', code='name invalid')
        return name

    def clean_profession(self):
        profession = self.cleaned_data['profession']
        if not re.match('[\u4e00-\u9fa5]+', profession):
            raise forms.ValidationError('职业输入有误', code='profession invalid')
        return profession

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )
