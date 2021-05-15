from django.db import models

# Create your models here.
class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 100)
    writer = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title
    
    