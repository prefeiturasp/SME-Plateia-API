from django.contrib import admin
from .models import Inscription


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'eventid', 'presence', 'priority', 'state', 'waitinglist', 'createdate')
    search_fields = ('id', 'eventid', 'eventid__showid')

    def user(self, obj):
        return obj.userid.name

    def waitinglist(self, obj):
        return 'Sim' if obj.waiting_list else 'Não'
