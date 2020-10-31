from django.db import models  
class Abc(models.Model):   
    name = models.CharField(max_length=100)    
    number = models.CharField(max_length=15)  
    class Meta:  
        db_table = "abc"  
