from django.contrib import admin
from django.contrib.auth.models import Group
from account.models import Users
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UsersAdmin(BaseUserAdmin):
    list_display = ('username','gender','account_open','absent','present')
    fieldsets = ()
    search_fields = ("username",)
    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields':("username",),
        }),
    )
    ordering = ("-account_open",)
admin.site.register(Users,UsersAdmin)
admin.site.unregister(Group)