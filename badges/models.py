from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

"""
Model3d
- Nom utilisateur
- Image
- Vue
"""
class Model3d(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='models_3d/', blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} ({self.views})"

"""
Badge
- Nom 
- Description
"""

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

"""
UserBadge
- Nom utilisateur
- badge
- date_obtention
"""
class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_obtention = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.badge} ({self.date_obtention})"



