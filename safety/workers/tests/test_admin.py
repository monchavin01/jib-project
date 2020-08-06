
from django.contrib import admin
from ..admin import WorkerAdmin
from django.test import TestCase
from ..models import Worker


class WorkerAdninTest(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Worker], WorkerAdmin))

    def test_admin_should_set_list_display(self):
        expected = (
             'first_name',
            'last_name',
            'is_available',
            'primary_phone',
            'secondary_phone',
        )
        self.assertEqual(WorkerAdmin.list_display, expected)

    def test_admin_should_set_list_filter(self):
        expected = (
              'is_available',
        )
        self.assertEqual(WorkerAdmin.list_filter, expected)
