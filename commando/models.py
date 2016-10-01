from django.db import models

# Create your models here.
class Item(models.Model):
	command = models.CharField(max_length=200, default = "")
	description = models.CharField(max_length=400, default = "")
	category = models.CharField(max_length=200, default = "System")
	def __unicode__(self):
		return self.command