from django.db import models

# Create your models here.
class WiseQuotes(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)    
    date = models.DateField(auto_now_add=True)    
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title