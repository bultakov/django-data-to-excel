from django.db import models


class UserData(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    about = models.TextField(max_length=5000)

    class Meta:
        verbose_name = 'User Data'
        verbose_name_plural = 'User Data'

    def __str__(self):
        return self.name
