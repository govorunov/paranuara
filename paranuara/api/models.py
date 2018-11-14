from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

# Create your models here.


class Companies(models.Model):
    """
    Companies model
    """
    index = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    company = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return "%s" % self.company


class ListField(models.TextField):

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, ListField):
            return value
        if value is None:
            return value
        return value.split(self.token)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return self.to_python(value)

    # def get_db_prep_value(self, value, connection, prepared=False):
    #     value = super().get_db_prep_value(value, connection, prepared)
    #     if value is not None:
    #         return connection.Database.Binary(value)
    #     return value

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, list) or isinstance(value, tuple) or isinstance(value, ListField))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


# class Tags(models.Model):
#     """
#     Tags model
#     """
#     name = models.CharField(max_length=32, unique=True)
#
#     def __str__(self):
#         return "%s" % self.name
#
#
# class Fruits(models.Model):
#     """
#     Fruits model
#     """
#     name = models.CharField(max_length=32, unique=True)
#
#     def __str__(self):
#         return "%s" % self.name
#
#
# class Vegetables(models.Model):
#     """
#     Vegetables model
#     """
#     name = models.CharField(max_length=32, unique=True)
#
#     def __str__(self):
#         return f"{self.name}"


class People(models.Model):
    """
    People Model
    """
    index = models.PositiveIntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=128, blank=True, null=True)
    _id = models.CharField(max_length=128, blank=True, null=True)
    guid = models.CharField(max_length=128, blank=True, null=True)
    has_died = models.BooleanField(default=False, blank=True, null=True)
    balance = models.CharField(max_length=64, blank=True, null=True)
    picture = models.CharField(max_length=256, blank=True, null=True)
    age = models.PositiveIntegerField(default=0, blank=True, null=True)
    eyeColor = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    registered = models.DateTimeField(blank=True, null=True)
    greeting = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Companies, related_name="employees", blank=True, null=True, on_delete=models.CASCADE)
    favourite_fruits = ListField(blank=True, null=True)
    favourite_vegetables = ListField(blank=True, null=True)
    tags = ListField(blank=True, null=True)
    friends = models.ManyToManyField(
        to='self',
        related_name='frended',
        blank=True,
        symmetrical=False)

    class Meta:
        db_table = 'people'

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self._id}"

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


# class Friends(models.Model):
#     """
#     Friend model
#     """
#
#     person_index = models.ForeignKey('People',  related_name='friends', on_delete=models.CASCADE)
#     friend_index = models.ForeignKey('People', related_name='+', on_delete=models.CASCADE)
