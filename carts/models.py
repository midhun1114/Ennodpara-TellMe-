from django.db import models

# Create your models here.
class cart(models.Model):
    title = models.TextField(blank=False, null=True)
    description= models.TextField(blank=False ,null=True )
    song=models.TextField(blank=True,null=True)
    name2=models.TextField(blank=True, null=True ,default="Anonymous")



