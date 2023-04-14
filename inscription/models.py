from django.db import models
from event.models import Event
from user.models import User
from .utils import dia_da_semana


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

    def get_ticket_dict_raw(self):
        ticket = {
            'inscricao_id': self.id,
            'nome': self.userid.name,
            'rf': self.userid.rf,
            'evento':  self.eventid.showid.name,
            'data': self.eventid.presentationdate,
            'horario': self.eventid.schedule.time(),
            'local': self.eventid.local,
            'endereco': self.eventid.address,
            'categoria': self.eventid.showid.showtypeid.name,
            'ingressos_por_membro': self.eventid.ticketbymember
        }
        return ticket

    def get_ticket_dict(self):
        ticket = {
            'inscricao_id': str(self.id),
            'nome': self.userid.name,
            'rf': self.userid.rf,
            'evento':  self.eventid.showid.name,
            'data': '{} - {}'.format(self.eventid.presentationdate.strftime("%d/%m/%Y"), dia_da_semana(self.eventid.presentationdate)),
            'horario': self.eventid.schedule.strftime("%H:%M"),
            'local': self.eventid.local,
            'endereco': self.eventid.address,
            'categoria': self.eventid.showid.showtypeid.name,
            'ingressos_por_membro': 'Vale ' + str(self.eventid.ticketbymember) + ' ingresso(s)'
        }
        return ticket

    def ticket_to_string(self, ticket_dict):
        return f"""N°: {ticket_dict["inscricao_id"]}
    Servidor: {ticket_dict["nome"]}
    RF: {ticket_dict["rf"]}
    Evento: {ticket_dict["evento"]}
    Data: {ticket_dict["data"]}
    Horário: {ticket_dict["horario"]}
    Local: {ticket_dict["local"]}
    Endereço: {ticket_dict["endereco"]}
    Categoria: {ticket_dict["categoria"]}
    {ticket_dict["ingressos_por_membro"]}"""
