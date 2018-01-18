from django.db import models

# Create your models here.


class PersonalDetail(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    year=models.IntegerField()
    university=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)


    def __str__(self):
        return self.name






