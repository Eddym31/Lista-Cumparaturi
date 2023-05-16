from django.db import models

class Products(models.Model):
    product = models.CharField(max_length=100)
    cumparat = models.BooleanField(default=False)

    def __str__(self):
        return self.product + '-->' + str(self.cumparat)
    
        
    
