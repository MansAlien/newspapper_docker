from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message']
    search_fields = ['user__username', 'change_message']


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
                    (None, {
                        "fields": ('age',),}),
                )
    add_fieldsets = UserAdmin.add_fieldsets + (
                    (None, {
                        "fields": ('age',),}),
                )
    
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(LogEntry, LogEntryAdmin)
