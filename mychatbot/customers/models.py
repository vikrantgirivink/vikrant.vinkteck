from django.db import models

# Create your models here.
class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    box= models.CharField("Text",max_length=255,blank=True, default='')
    #createdAt=models.DateTimeField("Created At",auto_now_add=True)
    
    def __str__(self):
        
        return self.box
    '''class Meta:
        ordering = ['created']'''