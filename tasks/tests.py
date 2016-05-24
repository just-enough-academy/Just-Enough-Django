from django.utils import timezone
from django.test import TestCase
from .models import Task

from django.test import Client


# Create your tests here.
class HappyPathTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_creating_a_new_task(self):
        self.assertFalse(Task.objects.exists())
        ## Pre-conditions above...
        
        Task.objects.create(text='Do you care?')
        
        ## Post-conditions below...
        self.assertTrue(Task.objects.exists())
        self.assertEqual(Task.objects.count(), 1)
        
        task = Task.objects.first()
        
        self.assertFalse(task.complete)
        self.assertTrue(task.created_on < timezone.now())
        
    def test_editing_a_task(self):
        Task.objects.create(text='What, still no caring?')
        
        task = Task.objects.first()
        
        self.assertFalse(task.complete)
        
        task.complete=True; task.save()
        
        self.assertTrue(Task.objects.first().complete)
        
    def test_CRUD_via_website(self):
        Task.objects.create(text='Why do I keep making these up?')
        
        self.assertEqual(Task.objects.count(), 1)
        
        self.assertContains(c.get('/tasks/'), "Why do I keep making these up?")
        
        self.client.post('/tasks/new', { "text": "Another of these?" })
        
        self.assertEqual(Task.objects.count(), 2)
        
        self.assertContains(self.client.get('/tasks/'), Task.objects.last().text)