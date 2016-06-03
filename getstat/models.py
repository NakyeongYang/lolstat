from django.db import models

# Create your models here.
class Stat(models.Model):
	id=models.CharField(max_length=20,primary_key=True)
	tier=models.CharField(max_length=10)
	division=models.IntegerField()
	point=models.IntegerField()