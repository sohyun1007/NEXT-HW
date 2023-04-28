from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Code(models.Model):
    title = models.CharField(max_length=50, default="")
    code = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="codes", null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
   code = models.ForeignKey(Code, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True)

   def __str__(self):
       return self.content