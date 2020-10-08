from django.db import models

# Create your models here.
class employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=254)
    employee_id=models.BigIntegerField()