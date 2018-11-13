from django.contrib import admin
from .models import People, Companies, Fruits, Vegetables, Tags

# Register your models here.
admin.site.register(People, )
admin.site.register(Companies)
admin.site.register(Fruits)
admin.site.register(Vegetables)
admin.site.register(Tags)
