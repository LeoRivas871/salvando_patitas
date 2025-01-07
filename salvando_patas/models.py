from django.db import models

#Modelo para salvando patitas
class Organization(models.Model):
    name = models.CharField(max_length=100)
    mission = models.TextField()
    vision = models.TextField()
    logo = models.ImageField(upload_to='logos/',blank=True,null=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

#Modelo para 'quienes somos'
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/',blank=True,null=True)

#Modelo para que hacemos
class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/',blank=True,null=True)
    date = models.DateField(blank=True,null=True)

#Modelo para problematica
class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

#Modelo para como ayudar
class HelpOption(models.Model):
    title = models.CharField(max_length=200)
    description = models.ImageField(upload_to='help/', blank=True,null=True)

#Modelo para recursos
class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    link = models.URLField(blank=True,null=True)
    file = models.FileField(upload_to='resources/',blank=True,null=True)

class Donation(models.Model):
    donor_name = models.CharField(max_length=100,blank=True,null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(auto_now_add=True)
    messagge = models.TextField(blank=True,null=True)