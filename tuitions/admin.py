from django.contrib import admin
from . import models

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}

admin.site.register(models.Tuitions)
admin.site.register(models.Subjects, SubjectAdmin)
