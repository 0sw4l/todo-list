from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'last_name',
        'first_name',
        'email',
        'phone'
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'category',
        'description',
        'created',
        'end_date',
        'success'
    ]
