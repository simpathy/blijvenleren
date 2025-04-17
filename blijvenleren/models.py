from django.db import models
from django.contrib.auth.models import User
from .constants import STATUS_CHOICES, PENDING


class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    user_roles = models.ManyToManyField(User, related_name='user_roles')

    def __str__(self):
        return self.name

class ApplicationScope(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resource(models.Model):

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.resource.title}"
