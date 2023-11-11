from django.db import models

class user(models.Model):
    login = models.CharField(max_length=8,blank=False)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f'{self.login}'