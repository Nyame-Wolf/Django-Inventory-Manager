from django.db import models

from django.contrib.auth import get_user_model


class Asset(models.Model):
    STATUS_CHOICES = (
        ('assigned', 'Assigned'),
        ('unassigned', 'UnAssigned'),
        ('lost', 'Lost'),
        ('lost & found', 'Lost and Found'),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=25)
    org_serial_code = models.CharField(max_length=25)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='assigned')
    date_bought = models.DateTimeField(auto_now_add=True)
    extra_info = models.TextField()

    def __str__(self):
        return self.name
