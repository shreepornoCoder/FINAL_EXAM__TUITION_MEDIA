from django.db import models
from django.contrib.auth.models import User

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
]


# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(to=User, related_name="profile", on_delete=models.CASCADE) 
    educational_institute = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    gender = models.CharField(choices=GENDER, max_length=10)

    def __str__(self):
        return f"{self.user.username}"


