from django.db import models

# Posting model to collect data from scraping
class Headline(models.Model):
  title = models.CharField(max_length=200)
  url = models.TextField(default='')
  date = models.CharField(max_length=64)
  replies = models.IntegerField(default=0)
  views = models.IntegerField(default=0)
  
  def __str__(self):
    return self.title