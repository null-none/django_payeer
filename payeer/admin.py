from django.contrib import admin
from .models import PSForUser


class PSForUserInline(admin.TabularInline):
    model = PSForUser
