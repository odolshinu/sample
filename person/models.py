from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)

    def __str__(self):
         return self.first_name

    def save(self, *args, **kwargs):
         super(Person, self).save(*args, **kwargs)
         return True

class Blog(models.Model):
    title = models.CharField(max_length=20)
    creator = models.ForeignKey(Person)

class Topping(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
         return self.name
    def get_name(self):
         return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=10)
    toppings = models.ManyToManyField(Topping)
