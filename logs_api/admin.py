from django.contrib import admin

from logs_api.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass