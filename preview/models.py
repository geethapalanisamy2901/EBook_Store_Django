from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BookDetails(models.Model):
    book_name = models.CharField(max_length=150)
    author = models.TextField(max_length=150)
    description = models.TextField(
        max_length=150, default='No description', editable=True)
    price = models.TextField(max_length=150)
    rating = models.TextField(max_length=150)


class UserDetails(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)


def sample_view(request):
    current_user = request.user
    print(current_user.id)
