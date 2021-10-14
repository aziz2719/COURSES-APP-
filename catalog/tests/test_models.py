from django.test import TestCase
from categorys.models import Course

class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(name='Название курса')

    def test_first_name_label(self):
        author = Course.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Название курса')

    def test_first_name_max_length(self):
        author = Course.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_object_first_name(self):
        author = Course.objects.get(id=1)
        expected_object_name = f'{author.name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Course.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), 'course/1')

