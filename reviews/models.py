from django.db import models
from uuid import uuid4


# Create your models here.
class Review(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    full_name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(unique=True)
    comment = models.TextField()
    ratings = models.PositiveSmallIntegerField()
    verify = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    # Sort data in descending order
    class Meta:
        ordering = ['-date']

    def __str__(self) -> str:
        return f'{self.email}'
