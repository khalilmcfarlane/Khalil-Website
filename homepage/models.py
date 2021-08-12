from django.db import models


# Create your models here.
class HomePage(models.Model):
    title = models.CharField(max_length=50)
    about_me_title = models.CharField(max_length=500)
    about_me_description = models.TextField()
    self_image = models.ImageField(height_field=15, width_field=15)
    linked_in_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.title
