from django.db import models


class Users(models.Model):
    name = models.CharField('name', max_length=10)

    def __str__(self):
        return self.name
