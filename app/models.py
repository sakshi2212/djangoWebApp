from django.db import models  
class Movie(models.Model):   
    name = models.CharField(max_length=100)    
    year = models.CharField(max_length=4) 
    genre =  models.CharField(max_length=20) 
    class Meta:  
        db_table = "movie"  
