from django.db import models

from django.db import models

# Create your models here.

class Expenses(models.Model):
    date = models.DateTimeField(auto_now=True)
    title = models.TextField(null=False, max_length=20)
    description = models.TextField()
    catagory = models.TextField()
    amount = models.FloatField()

    def __str__(self):
        return self.title
