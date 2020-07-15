from django.db import models


# Create your models here.

class Tour(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    category = models.ForeignKey('Category' ,null=True ,on_delete=models.SET_NULL)
   

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='demoapp/' , null=True)
    def __str__(self):
        return self.category_name
        

   
    



