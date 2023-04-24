from django.contrib import admin
from .models import Event, Eventhistory, Comment, Genre, Genreshowtype, File, Show, Showtype


admin.site.register(Event)
admin.site.register(Eventhistory)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Genreshowtype)
admin.site.register(File)
admin.site.register(Show)
admin.site.register(Showtype)
