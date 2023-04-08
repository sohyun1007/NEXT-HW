from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    end_date = models.DateTimeField()

    def deadline(self):
        end_date = self.end_date
        today = timezone.now()
        d_day = (end_date - today).days
        return d_day

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['end_date']