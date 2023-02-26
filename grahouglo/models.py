from django.db import models


class Contact(models.Model):
    name= models.CharField(max_length=120)
    number= models.CharField(max_length=30)
    email=models.EmailField(max_length=120)
    message=models.TextField(max_length=300)

    def __str__(self):
        return self.name
