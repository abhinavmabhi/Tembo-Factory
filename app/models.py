from django.db import models

class Services(models.Model):
    type_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    head_image = models.ImageField(upload_to='services')
  
    
    def __str__(self):
        return self.type_name



class Contact(models.Model):
    choose_service=models.ForeignKey(Services,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
