from django.db import models

class user(models.Model):
    login = models.CharField(max_length=8,blank=False)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return f'{self.login}'

class image(models.Model):
    # name = models.CharField(max_length=20, blank=False)
    img = models.ImageField(upload_to="media/",null=True, blank=True)


class hydrogenPlaces(models.Model):
    positionName = models.CharField(max_length=10, blank=False)
    x = models.IntegerField(blank=False)
    y = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.positionName}'

class carbonPlaces(models.Model):
    positionName = models.CharField(max_length=10, blank=False)
    x = models.IntegerField(blank=False)
    y = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.positionName}'

