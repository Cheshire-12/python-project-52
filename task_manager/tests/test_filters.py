from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.models import Task

User = get_user_model()


class TaskFilterTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        self.factory = RequestFactory()
        
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)

        self.status = Status.objects.get(pk=1)
        self.label = Label.objects.get(pk=1)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.create(
            name='Task 3',
            author=self.user2,
            status=self.status
        )

    def test_filter_by_status(self):
        filter_data = {'status': self.status.pk}
        task_filter = TaskFilter(data=filter_data, queryset=Task.objects.all())
        
        self.assertTrue(task_filter.is_valid())
        self.assertEqual(task_filter.qs.count(), 2)

    def test_filter_by_executor(self):
        filter_data = {'executor': self.user2.pk}
        task_filter = TaskFilter(data=filter_data, queryset=Task.objects.all())
        
        self.assertTrue(task_filter.is_valid())
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_filter_by_label(self):
        filter_data = {'labels': [self.label.pk]}
        task_filter = TaskFilter(data=filter_data, queryset=Task.objects.all())
        
        self.assertTrue(task_filter.is_valid())
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_filter_self_tasks(self):
        request = self.factory.get('/')
        request.user = self.user1 

        filter_data = {'self_tasks': 'on'}
        
        task_filter = TaskFilter(
            data=filter_data, 
            queryset=Task.objects.all(), 
            request=request
        )
        
        self.assertTrue(task_filter.is_valid())
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)