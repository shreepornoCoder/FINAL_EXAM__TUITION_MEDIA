from django.db import models
from user.models import User

MEDIUM = [
    ("Bangla", "Bangla"),
    ("English", "English")
]
TUITOR = [
    ("Male", "Male"),
    ("Female", "Female"),
]
GRADE =[
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('HSC-1st Year', 'HSC-1st Year'),
    ('HSC-2nd Year', 'HSC-2nd Year'),
    ('Admission Test', 'Admission Test')
]

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Tuitions(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(choices=GRADE, max_length=100)
    medium = models.CharField(choices=MEDIUM, max_length=10)
    prefered_tutor = models.CharField(choices=TUITOR, max_length=10)
    stu_gender = models.CharField(choices=TUITOR, max_length=10, default="Male")
    salary = models.IntegerField()
    descripition = models.TextField()
    subjects = models.ManyToManyField(to=Subjects, related_name="subject")
    location = models.CharField(max_length=300)
    have_tuitor = models.BooleanField(default=False)
    is_applied = models.BooleanField(default=False)
    extra_need = models.TextField(default="Null")
    
    def __str__(self):
        return f"{self.name}"
    
# reviews
RATINGS = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Reviews(models.Model):
    reviewer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    tuition = models.ForeignKey(to=Tuitions, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.CharField(choices=RATINGS, max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review has given by {self.reviewer.user.username}"