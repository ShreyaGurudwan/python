from django.contrib import admin

# Register your models here.
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')  # columns to show
    search_fields = ('name', 'age')        # search bar
    list_filter = ('age',)                   # filter sidebar

admin.site.register(Student , StudentAdmin)