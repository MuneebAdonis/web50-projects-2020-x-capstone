from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.
class Title(models.Model):
    title_type = models.CharField(max_length=50)
    def __str__(self):
        return self.title_type

class User(AbstractUser):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True)
    signup = models.BooleanField(default=False)
    pass

# define str to easily see whats what in admin
class Stain(models.Model):
    stain_type = models.CharField(max_length=200)
    def __str__(self):
        return self.stain_type

class System(models.Model):
    system_type = models.CharField(max_length=200)
    def __str__(self):
        return self.system_type

class Tissue(models.Model):
    tissue_type = models.CharField(max_length=200)      
    system = models.ForeignKey(System, on_delete=models.CASCADE)  
    def __str__(self):
        return self.tissue_type
    def serialize(self):
        return {"tissue":self.tissue_type,
                "system":self.system.system_type}

class Gender(models.Model):
    gender_type = models.CharField(max_length=50)
    def __str__(self):
        return self.gender_type

class Diagnosis(models.Model):
    WHO_diagnosis = models.CharField(max_length=200)
    def __str__(self):
        return self.WHO_diagnosis

class Slide(models.Model):
    date = models.DateField(default = now)
    age= models.PositiveIntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=1)
    tissue = models.ForeignKey(Tissue, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, default=1)
    stain = models.ForeignKey(Stain, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    clinic_info = models.TextField(max_length=5000, null=True)

class Comment(models.Model):
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default = now)
    comment = models.TextField(max_length=5000)
    def __str__(self):
        return f"{self.person.username} on {self.date.strftime('%d %b %Y')}"
    def serialize(self):
        return {
            "comment":self.comment,
            "person":f"{self.person.title} {self.person.first_name[0]} {self.person.last_name}",
            "person_id":self.person.id,
            "date_formatted":self.date.strftime('%d %b %Y').lower(),
            "date": self.date
            }