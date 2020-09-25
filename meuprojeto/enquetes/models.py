from django.db import models

# Create your models here.
class Enquete(models.Model):
	texto = models.CharField(max_length = 30)
	data_publicacao = models.DateField()