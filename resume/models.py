from django.db import models


# Create your models here.
class Resume(models.Model):
    resume_title = models.CharField()
    resume_space = models.TextField()

    def __str__(self):
        return self.resume_title
