from django.db import models
from uuid import uuid4


# Create your models here.
class Category(models.TextChoices):
    WEB = 'Web'
    CLOUD = 'Cloud'


class Project(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=255, unique=True, db_index=True)
    category = models.CharField(max_length=50, choices=Category.choices)
    cover_image = models.ImageField(upload_to='portfolio/peter/')
    description = models.TextField()
    project_url = models.URLField()
    github_url = models.URLField()
    date = models.DateField(auto_now_add=True)

    # Sort data in descending order
    class Meta:
        ordering = ['-date']
    
    def __str__(self) -> str:
        return f'{self.title}'
