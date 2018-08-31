from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class VehiclePart(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2, default='0.00')
    description = models.TextField(max_length=1000,
                                   default='Add some description')
    pub_date = models.DateTimeField(
        default=str(datetime.now())[:16], auto_now=False, auto_now_add=False)
    section = models.ForeignKey(
        'Section',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey('auth.User',
                             null=True, blank=True,
                             on_delete=models.SET_NULL)

    def __str__(self):
        return "{}: price - {} USD. Published at: {}. Section: {}".format(
            self.name, self.price, str(self.pub_date)[:-9], self.section.name
        )


class Section(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,
                                   default='Add some description')
    user = models.ForeignKey('auth.User',
                             null=True, blank=True,
                             on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}: {self.description[:5]}..."
