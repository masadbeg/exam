from django.db import models


class Profile(models.Model):
		first_name = models.CharField(max_length=50)
		last_name = models.CharField(max_length=100)
		birth_date = models.DateField()
		is_worker = models.BooleanField(default=True)

    def __str__(self):
    full_name = f'{first_name} {last_name}'
    return full_name
    
#Напишите для этой модели сериализатор для реализации **CRUD** функционала.
# Примите во внимание, что при чтении данной модели имя и фамилия должны быть объединены в одно поле full_name

from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Profile

 
class ProfileSerializers(models.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')


 
