from django.db import models



# Create your models here.

class bookdetails(models.Model):	
	book_name=models.CharField(max_length=50,blank=True);
	isbn_number=models.IntegerField(blank=True);
	price=models.FloatField();
	author=models.CharField(max_length=50);
