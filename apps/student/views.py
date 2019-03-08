from django.shortcuts import render
from student.models import Student
from student.forms import StudentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data  # 经过验证后的数据
            student = Student()  # 生成一个空的对象
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('student:index'))
    ctx = {'data': students, 'form': form}
    return render(request, 'student/index.html', ctx)
