from django.contrib import admin

# Register your models here.


from .models import Details, College

admin.site.register(Details)
admin.site.register(College)
