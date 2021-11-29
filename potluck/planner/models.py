from django.db import models
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
  def __str__(self):
    return self.email

  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  msg = models.TextField(max_length=2000)
  time_sent = models.DateTimeField(default=now)
  msg_read = models.BooleanField(default=False)


class Event(models.Model):
  def __str__(self):
    return self.name

  name = models.CharField(max_length=200)
  desc = models.TextField(max_length=2000)
  image = models.ImageField(upload_to='pictures', default='pictures/noimg.jpg')
  location = models.CharField(max_length=200)
  start_day = models.DateField()
  end_day = models.DateField()	
  start_time = models.TimeField()
  end_time = models.TimeField()	
  created_by= models.CharField(max_length=100, default='admin@admin.com')

class Item(models.Model):
  def __str__(self):
    return self.name

  name = models.CharField(max_length=200)
  category = models.CharField(max_length=200)
  userId = models.IntegerField()	
  image = models.ImageField(upload_to='pictures', default='pictures/noimg.jpg')
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  created_by = models.CharField(max_length=100, default='admin@admin.com')