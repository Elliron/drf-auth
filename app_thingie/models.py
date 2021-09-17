from django.db import models
from django.contrib.auth import get_user_model

class App_thingie(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title