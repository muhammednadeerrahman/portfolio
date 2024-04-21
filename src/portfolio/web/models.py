from django.db import models
SKILL_TYPE = (
    ("frontend","Frontend"),
    ("backend","Backend"),
    ("devops","Devops"),
    ("API_development","API_Development"),
)
class Skill(models.Model):
    skill_image = models.FileField(upload_to="skills", null=True, blank=True)
    skill_name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=255,choices=SKILL_TYPE,)


    def __str__(self):
        return self.skill_name
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
    


    def __str__(self):
        return self.name
    

