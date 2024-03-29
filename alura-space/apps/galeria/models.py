from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Photograph(models.Model):

    CATEGORY_OPTIONS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta"),
        ("LUA", "Lua"),
    ]

    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    modified = models.DateTimeField(auto_now=True, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default="")
    description = models.TextField(null=False, blank=False)
    file = models.ImageField(upload_to="photographs/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=True)
    photograph_date = models.DateField(default=datetime.datetime.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self) -> str:
        return self.name