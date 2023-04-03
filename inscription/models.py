from django.db import models
from event.models import Event
from user.models import User


class Inscription(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    userid = models.ForeignKey(User, models.DO_NOTHING, to_field='id', db_column='UserId')
    eventid = models.ForeignKey(Event, models.DO_NOTHING, db_column='EventId')
    presence = models.BooleanField(db_column='Presence')
    priority = models.IntegerField(db_column='Priority')
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'Inscription'
        managed = False


# def ticket_to_string(ticket):
#     return f'N°: {ticket.InscriptionId}\n' \
#            f'Servidor: {ticket.Name}\n' \
#            f'RF: {ticket.RF}\n' \
#            f'Evento: {ticket.EventName}\n' \
#            f'Data: {ticket.PresentationDate.strftime("%d/%m/%Y")} - {ticket.DayOfWeek}\n' \
#            f'Horário: {ticket.Schedule.strftime("%H:%M")}\n' \
#            f'Local: {ticket.Local}\n' \
#            f'Endereço: {ticket.Address}\n' \
#            f'Categoria: {ticket.ShowType}\n' \
#            f'Vale {ticket.TicketByMember} ingresso(s)'
