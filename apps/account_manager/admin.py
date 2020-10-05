from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _

from apps.account_manager.models import BaseUser, Account, Profile
from apps.account_manager.services import user_create
from django.contrib.auth.admin import UserAdmin

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'billingAddress', 'isActive', 'website','created_at', 'updated_at')
    readonly_fields= ('id', 'created_at', 'updated_at')
    search_fields = ('name','website')

    list_filter = ('isActive',)

    fieldsets = (
        (None, {'fields': ('id','isActive')}),
        (_('Personal info'), {'fields': ('name','website', 'billingAddress')}),
        (_('Important dates'), {'fields': ('created_at','updated_at')}),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields= ('id', 'created_at', 'updated_at')
    search_fields = ('name',)

    list_filter = ()

    fieldsets = (
        (None, {'fields': ('id',)}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Important dates'), {'fields': ('created_at','updated_at')}),
    )

@admin.register(BaseUser)
class BaseUserAdmin(UserAdmin):
    list_display = ('email', 'is_admin', 'is_superuser', 'is_active', 'created_at', 'updated_at')
    readonly_fields= ('last_login','id', 'created_at', 'updated_at')
    search_fields = ('email','account','profile')

    list_filter = ('is_active', 'is_admin', 'is_superuser','account','profile')

    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','account','profile')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'created_at','updated_at')}),
    )

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            user_create(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
