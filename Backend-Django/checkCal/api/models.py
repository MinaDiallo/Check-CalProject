from django.db import models

# Create your models here.
class Foods(models.Model):
    name= models.CharField(max_length=30,unique=True, null=False)
    description = models.TextField(max_length=200, null=True)
    rate= models.IntegerField(default=0, null=False)
    
    def __str__(self):
        return self.name