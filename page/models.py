from django.db import models

class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ident = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    cel = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    adrress = models.CharField(max_length=100)

class Wine_letter(models.Model):
    id_wine = models.AutoField(primary_key=True)
    wine_type = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    yaer = models.DateTimeField()
    value = models.FloatField()

class sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    client =models.ForeignKey(Person,on_delete=models.CASCADE)
    prod = models.ManyToManyField(Wine_letter)
    total = models.FloatField()
    
    
    
