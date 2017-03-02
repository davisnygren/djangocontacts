from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Your phone number must be in the '+999999999' format.")
    phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    add_date = models.DateTimeField('date added')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now

    @classmethod
    def create(cls, first_name, last_name, email, address, phone, add_date):
        contact = cls(first_name=first_name, last_name=last_name, email=email, address=address, phone=phone, add_date=add_date)
        return contact
