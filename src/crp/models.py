from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
consulatunt_name = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
contr_name = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]



class cpt(models.Model):
   project_name = models.CharField(max_length=50)
   contract_number = models.DecimalField(max_digits=14, decimal_places=0)
   contract_date = models.DateField(auto_now=False, auto_now_add=False)
   consultant_name = models.CharField(max_length=50,choices=consulatunt_name )
   contr_name = models.CharField(max_length=50,choices=contr_name )



   def __str__(self):
          return self.project_name

class Create(models.Model):
   project_name = models.CharField(max_length=50)
   contract_number = models.DecimalField(max_digits=14, decimal_places=0)
   contract_date = models.DateField(auto_now=False, auto_now_add=False)
   contr_name = models.CharField(max_length=50,choices=contr_name )



   def __str__(self):
          return self.project_name

