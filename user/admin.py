from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserModelAdmin(UserAdmin):
    model = User
    list_display = ('id', 'name', 'email', 'date_joined', )
    search_fields = ('name', )
    search_help_text = 'Pesquise por nome.'

    # fieldsets = (('Acesso', {'fields': ('username', 'password')}),
    #              ('Permissões', {'fields': ('is_active', 'is_staff', 'groups', )}), ('Datas importantes', {'fields': ('last_login', 'date_joined')}))
    # add_fieldsets = (('Acesso', {'fields': ('username', 'password1', 'password2')}),
    #                  ('Permissões', {'fields': ('is_active', 'is_staff', 'groups', )}), ('Datas importantes', {'fields': ('last_login', 'date_joined')}))


admin.site.register(User, CustomUserModelAdmin)
