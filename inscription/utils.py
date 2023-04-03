from datetime import datetime
from django.template.loader import render_to_string
from django.http import HttpResponse
from io import BytesIO
# from reportlab.pdfgen import canvas


# def generate_base64_pdf_ticket(ticket):
#     template = 'voucher.html',
#     body = {
#         # **ticket
#     }
#     html = render_to_string(template, {'context': body})
#     # template
#     # return response


def dia_da_semana(data):
    # Converter a string de entrada para um objeto datetime.date
    data_obj = data.date()

    # Definir os nomes dos dias da semana
    dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

    # Obter o índice do dia da semana (0 = segunda-feira, 1 = terça-feira, etc.)
    dia_da_semana_idx = data_obj.weekday()

    # Retornar o nome do dia da semana correspondente
    # return dias_da_semana[dia_da_semana_idx]

    return dias_da_semana[dia_da_semana_idx]
