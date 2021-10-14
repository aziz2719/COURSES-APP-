from django.test import TestCase
from django.urls import reverse

from categorys.models import Course

class CourseListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_course = 13
        for name_id in range(number_of_course):
            Course.objects.create(
                name=f'Верстальщик {name_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('course/1')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cource'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('course'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['course_list']), 10)

    def test_lists_all_authors(self):
        response = self.client.get(reverse('course')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['course_list']), 3)
