from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=255)

class Team(models.Model):
    name_avenger = models.ForeignKey(Name, models.SET_NULL, 'avenger', null=True)
    name = models.CharField('Имя героя', max_length=255)
    gender = models.CharField('Пол', max_length=255)
    ability = models.CharField('Способность', max_length=255)