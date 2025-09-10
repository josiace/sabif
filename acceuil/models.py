
from django.db import models

class Visite(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visite du {self.date.strftime('%d/%m/%Y %H:%M:%S')}"

# Create your models here.

class Contenus(models.Model):
    titre = models.CharField(max_length=100)
    blog = models.TextField()
    auteur = models.CharField(max_length=100)
    mail = models.EmailField()
    date_creation = models.DateTimeField(auto_now_add=True)
    lien = models.URLField(blank=True)
    num = models.IntegerField(blank=True)

    def __str__(self):
        return self.titre


class BlogImage(models.Model):
    contenu = models.ForeignKey(Contenus, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return f"Image de {self.contenu.titre}"

class Acceuilperso(models.Model):
    titre=models.CharField(max_length=100)
    description=models.TextField()
    disclaimer=models.TextField(blank=True)

    def __str__(self):
        return self.titre