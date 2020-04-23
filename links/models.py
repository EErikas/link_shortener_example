import string
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
class Link(models.Model):
    shortened_link = models.CharField(max_length=5, unique=True, default=get_random_string(5, allowed_chars=string.ascii_letters + string.digits))
    original_url = models.URLField(verbose_name='Original URL')
