from django.db import models
from user.models import UserModel
from tuitions.models import Tuitions

STATUS = [
    ("Pending", "Pending"),
    ("Selected", "Selected")
]

# Create your models here.
class UserTuitionHistory(models.Model):
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    tuition = models.ForeignKey(to="tuitions.Tuitions", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10, default="Pending")
    time = models.DateTimeField(auto_now_add=True)