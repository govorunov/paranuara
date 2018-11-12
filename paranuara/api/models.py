from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

# Create your models here.


class Company(models.Model):
    """
    Company model
    """
    index = models.IntegerField(primary_key=True, unique=True, blank=False, null=False, verbose_name=_("Company index"))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Company name"))

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    Person Model
    """
    _id = models.CharField(max_length=128, unique=True, blank=False, verbose_name=_("People ID"))
    guid = models.CharField(max_length=128, unique=True, blank=False, verbose_name=_("GUID"))
    index = models.PositiveIntegerField(primary_key=True, unique=True, blank=False, null=False, verbose_name=_("People Index"))
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("Name"))
    age = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name=_("Age"))
    has_died = models.BooleanField(default=False, verbose_name="Has this person died")
    balance = models.DecimalField(default=0.0, decimal_places=2, max_digits=32, verbose_name=_("Balance"))
    picture = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("Picture"))
    eye_color = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("Eye Color"))
    gender = models.CharField(max_length=16, blank=True, null=True, verbose_name=_("Gender"))
    company = models.ForeignKey('Company', related_name="company_staffs", blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Company ID"))
    email = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("Email"))
    phone = models.CharField(max_length=32, blank=True, null=True, verbose_name=_("Phone"))
    address = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("Address"))
    about = models.TextField(blank=True, null=True, verbose_name=_("About"))
    registered = models.DateTimeField(blank=True, null=True, verbose_name=_('Registered'))
    tags = models.TextField(blank=True, null=True, verbose_name=_("Tags"))
    favourite_food = models.TextField(blank=True, null=True, verbose_name=_("Favourite Food"))
    favourite_fruit = models.TextField(blank=True, null=True, verbose_name=_("Favourite Fruit"))
    favourite_vegetable = models.TextField(blank=True, null=True, verbose_name=_("Favourite Vegetable"))
    greeting = models.TextField(blank=True, null=True, verbose_name=_("Greeting"))

    class Meta:
        db_table = 'people'

    def __str__(self):
        return self.name

    # def __setattr__(self, attrname, val):
    #     setter_func = 'set_' + attrname
    #     if attrname in self.__dict__ and callable(getattr(self, setter_func, None)):
    #         super().__setattr__(attrname, getattr(self, setter_func)(val))
    #     else:
    #         super().__setattr__(attrname, val)
    #
    # def __getattr__(self, attrname):
    #     getter_func = 'set_' + attrname
    #     if attrname in self.__dict__ and callable(getattr(self, getter_func, None)):
    #         getattr(self, getter_func)(super().__getattr__(attrname))
    #     else:
    #         super().__getattr__(attrname)
    #
    # def set_foo(self, val):
    #     return val.upper()
    #
    # def get_breed(self, val):
    #     return self.name + ' belongs to ' + val + ' breed.'


class Friends(models.Model):
    """
    Friend model
    """

    person_index = models.ForeignKey('Person',  related_name='friends', on_delete=models.CASCADE)
    friend_index = models.ForeignKey('Person', related_name='+', on_delete=models.CASCADE)
