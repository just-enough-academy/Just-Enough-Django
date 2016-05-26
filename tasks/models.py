from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    """
    Represents a textual reminder of what I need to do and whether I've
    successfully completed it or not. Records the date and time of its
    creation so it can be listed by oldest items first.

    >>> Task.objects.count()
    0
    
    >>> do_something = Task.objects.create(text='Do something!')
    >>> do_something.complete
    False
    
    >>> import datetime
    >>> do_something.created_on is datetime.datetime.now()
    True

    >>> do_something.text
    "Do something!"

    >>> Task.objects.count()
    1
    
    >>> Task.objects.first() == do_something
    True

    >>> Task.objects.count(completed=True)
    0

    >>> do_something.created = True
    >>> do_something.save()
    >>> len(Task.objects.filter(completed=True))
    1
    """

    text = models.TextField()

    complete = models.BooleanField(default=False, null=False)

    created_on = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user=models.OneToOneField(User)

class Color(models.Model):
    hex_value=models.CharField(max_length=6)
    
    def __str__(self):
        return self.hex_value
    
class Label(models.Model):
    text=models.TextField(null=False, blank=False)
    
    color=models.ForeignKey(Color, null=True)
    
    def __str__(self):
        return "{label.text} ({label.color})".format(label=self)
    
    