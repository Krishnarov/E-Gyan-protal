from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Enquiry)
admin.site.register(models.Login)