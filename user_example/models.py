from django.db import models
from django.contrib.auth.models import User

class Index(models.Model):
    name  = models.CharField(max_length=25)
    email = models.EmailField(null=True)
    dob   = models.DateField(null=True)
    #user  = models.ForeignKey(User,on_delete=models.PROTECT)
