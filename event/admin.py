from django.contrib import admin
from .models import Event, Eventhistory, Comment, Genre, Genreshowtype, File, Show, Showtype


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'show', 'presentationdate', 'ticketquantity', 'ticketavailable', 'inscriptions', 'queuesize', 'queueremaining')

    def show(self, obj):
        return obj.showid.name

    def inscriptions(self, obj):
        return obj.inscription_set.count()


admin.site.register(Eventhistory)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Genreshowtype)
admin.site.register(File)
admin.site.register(Show)
admin.site.register(Showtype)
