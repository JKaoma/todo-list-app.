from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories (models.Model):
    name = models.CharField(max_length = 64)

class Task (models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField(default = '')
    date_created = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField()
    category_id = models.ForeignKey(Categories)
    marked_done = models.BooleanField()
    user_id = models.ForeignKey(User)
