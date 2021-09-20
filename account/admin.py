from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'nombre_apellido', 'cargo' ,'fecha_creacion', 'last_login', 'is_admin', 'is_active' )
    search_fields = ('email', 'nombre_apellido', 'cargo')
    readonly_fields = ('id', 'fecha_creacion', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(Account, AccountAdmin)
# Register your models here.
