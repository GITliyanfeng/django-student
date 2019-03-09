from django.test import TestCase
from student.models import Student
from django.test.client import Client
from django.urls import reverse


# 测试视图层  Client

# Create your tests here.
# 创建测试用例
class StudentTestCase(TestCase):
    # 初始化
    def setUp(self):
        Student.objects.create(
            name='测试用例',
            sex=1,
            email='test@qq.com',
            profession='测试部',
            qq='7899987890',
            phone='13131333313'
        )

    def test_create_and_str(self):
        student = Student.objects.create(
            name='测试用例',
            sex=1,
            email='test@qq.com',
            profession='测试部',
            qq='7899987890',
            phone='13131333313'
        )
        student_name = '<Student: 测试用例>'
        # 测试student的__str__方法是否返回正确的值
        self.assertEqual(str(student), student_name, 'student __str__ must be {}'.format(student_name))

    def test_filter(self):
        student = Student.objects.filter(name='测试用例')
        self.assertEqual(student.count(), 1, 'only one is right')

    def test_get_index(self):
        client = Client()
        response = client.get(reverse('student:index'))
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='测试用例',
            sex=1,
            email='test@qq.com',
            profession='测试部',
            qq='7899987890',
            phone='13131333313'
        )
        response = client.post(reverse('student:index'), data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')
        response = client.get(reverse('student:index'))
        self.assertTrue('测试用例'.encode('utf-8') in response.content, 'response content must contain "测试用例"')

