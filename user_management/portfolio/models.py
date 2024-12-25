from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='portfolio')
    projects = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"
