from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}_{1}/{2}'.format(instance.user.id,instance.user.username,filename)



class Layers(models.Model):
	user = models.ForeignKey(User,on_delete=models.PROTECT)
	name_of_layer = models.CharField(max_length=50)
	description = models.TextField(max_length=200)
	select_themes_CHOICES  = (
			('NON','None'),
			('CEN','Census'),
			('EDU','Education'),
			('RUL','Rural'),
			('WAT','Water'),
			('HEL','Health'),
			('OTH','Other'),
		)
	select_theme = models.CharField(max_length=6,choices=select_themes_CHOICES,default='None')
	if_other = models.CharField(max_length=50)
	source = models.CharField(max_length=50)
	types_CHOICES = (
			('NON','None'),
			('GJ','GeoJSON'),
			('EL','Excel'),
			('CV','CSV'),
			('GL','GML'),
			('ZS','Zipped Shapefile'),
			('KL','KML'),
			('PF','PDF'),
			('TF','TIF'),
			('PG','PNG'),
			('JG','JPEG'),
		)
	types = models.CharField(max_length=6,choices=types_CHOICES,default='None')
	style_file_available_CHOICES = (
			('NON','None'),
			('Y','Yes'),
			('N','No'),
		)
	style_file_available = models.CharField(max_length=3,choices=style_file_available_CHOICES,default='None')
	tool_used = models.CharField(max_length=50)
	layer = models.FileField(upload_to=user_directory_path)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name_of_layer

	def delete(self, *args, **kwargs): 					
		self.layer.delete()
		super().delete(*args,**kwargs)