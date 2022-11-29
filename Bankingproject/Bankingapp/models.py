
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


AccountType = (
    ('SA',  'Savings Account'),
    ('CA', 'Current Account'),
    ('ST' , 'Studetn Account'),
    ('NRI' , 'NRI Account'),

)

class MyModel(models.Model):
  acctype = models.CharField(max_length=6, choices=AccountType, default='Savings Account')
