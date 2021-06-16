#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cruddemo.settings')

import django
django.setup()

from crudapp.models import*
from faker import Faker
from random import *
faker = Faker()


def populate(n):
    # data is a list of lists
    for row in range(n):
        fsno = randint(1,9999)
        fsname = faker.name()
        fsclass=randint(1,100)
        fsaddress=faker.city()
        stud_record=Student.objects.get_or_create(sno=fsno,
        sname=fsname,sclass=fsclass,saddress=fsaddress)



populate(10)