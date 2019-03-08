from django.shortcuts import render
from student.models import Student
from student.forms import StudentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import View


# Create your views here.
# CBV 方式分离请求
class IndexView(View):
    template_name = 'student/index.html'

    @staticmethod
    def get_context():
        students = Student.objects.all()
        ctx = {
            'data': students
        }
        return ctx

    def get(self, request):
        ctx = self.get_context()
        form = StudentForm()
        ctx.update({
            'form': form
        })
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()  # 生成一个空的对象
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('student:index'))
        ctx = self.get_context()
        ctx.update({
            'form': form
        })
        render(request, self.template_name, ctx)
