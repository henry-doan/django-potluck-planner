from django.db import models

# Create your models here.
class Contact(models.Model):
  def __str__(self):
    return self.email

  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  msg = models.TextField(max_length=2000)


class Event(models.Model):
  def __str__(self):
    return self.name

  name = models.CharField(max_length=200)
  desc = models.TextField(max_length=2000)
  image = models.ImageField(upload_to='pictures', default='pictures/none/noimg.jpg')
  location = models.CharField(max_length=200)
  start_day = models.DateField()
  end_day = models.DateField()	
  start_time = models.TimeField()
  end_time = models.TimeField()	


class Item(models.Model):
  def __str__(self):
    return self.name

  name = models.CharField(max_length=200)
  category = models.CharField(max_length=200)
  userId = models.IntegerField()	
  image = models.ImageField(upload_to='pictures', default='pictures/none/noimg.jpg')
  event = models.ForeignKey(Event, on_delete=models.CASCADE)