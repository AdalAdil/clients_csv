from django.db import models


class Client(models.Model):
    category = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)
    birth_ate = models.DateField()

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        db_table = "client"