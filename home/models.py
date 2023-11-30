from django.db import models

# Create your models here.


class Home(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="images/", null=True)
