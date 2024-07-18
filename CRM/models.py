from django.db import models

# Create your models here.
class customers(models.Model):
    firstname= models.CharField(max_length=150)
    surname= models.CharField(max_length=150)
    username= models.CharField(max_length=150)
    email= models.EmailField(max_length=50)
    mobile_no= models.CharField(max_length=15)
    Address = models.CharField(max_length=200)

    def __str__(self):
        return self.username
