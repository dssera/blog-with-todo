from django.db import models
from django.contrib.auth.models import User



class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(TimeStampedModel):
    """Table for task in todo app"""
    # it's pretty common situation when you need to have status field
    # you can implement this by using Status class:
    class Status(models.TextChoices):
        # every task has 2 states: stored(finished) and current(in the proccess)
        CURRENT = "CR", "Current"
        STORED = "ST", "Stored"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Task\'s text')
    # why do we use charfield?
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.CURRENT)
    
    class Meta:
        ordering = ['-created_at', '-updated_at']
        indexes = [
            models.Index(fields=['-created_at', '-updated_at'])
        ]

    def __str__(self) -> str:
        return self.body[:20]

