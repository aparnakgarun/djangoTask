
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title



