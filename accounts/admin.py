from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, College

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','college', 'contact_num']
    search_fields = ['email', 'college', 'contact_num']



admin.site.register(College)
#unregistering the Group model
admin.site.unregister(Group)