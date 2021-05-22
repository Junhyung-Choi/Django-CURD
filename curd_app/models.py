from django.db import models

# Create your models here.
class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 100)
    writer = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/', default = "")

    def __str__(self):
        return self.title
    
class Store(models.Model):
    objects = models.Manager()
    tradename = models.CharField(max_length = 100)
    owner = models.CharField(max_length = 10)
    location = models.CharField(max_length = 100)
    jobdetail = models.TextField()
    wage = models.IntegerField()
    currentapplicant = models.IntegerField()
    isapply = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'images/', default = "")

    def __str__(self):
        return self.tradename

class Comment(models.Model):
    objects = models.Manager()
    store_id = models.ForeignKey(Store,on_delete=models.CASCADE, null = True)
    date = models.DateTimeField(auto_now_add = True)
    user = models.TextField(max_length = 20)
    content = models.TextField(max_length = 100)
    