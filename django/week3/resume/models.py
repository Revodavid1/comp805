from django.db import models

# Create your models here.

class Experience(models.Model):
	title = models.CharField(max_length=100,null=False, blank=False)
	location = models.CharField(max_length=100,null=False, blank=False)
	start_date = models.DateField(null=False, blank=False)
	end_date = models.DateField(null=False, blank=False)
	description = models.CharField(max_length=255, null=False, blank=True)

	def __str__(self):
		return self.title