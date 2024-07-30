from django.db import models


class List(models.Model):
    item_name = models.TextField()
    quantity = models.IntegerField()
    purchased = models.BooleanField(default=False)







