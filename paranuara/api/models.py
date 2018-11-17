from django.db import models
from .custom_fields import ListField


class Companies(models.Model):
    """
    Companies model
    """
    index = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return "%s" % self.company


class People(models.Model):
    """
    People Model
    """
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    _id = models.CharField(max_length=64, blank=True, null=True)
    guid = models.CharField(max_length=64, blank=True, null=True)
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
        return "%s" % self.name
