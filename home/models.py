from django.db import models

# Create your models her
class Resume(models.Model):
    title = models.CharField(max_length=100, default="My Resume")
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
