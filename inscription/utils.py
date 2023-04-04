import logging
import base64
import qrcode
from io import BytesIO
from django.template.loader import render_to_string
from django.conf import settings
from weasyprint import HTML

logger = logging.getLogger(__name__)


def generate_ticket_voucher(ticket_dict):
    html_string = render_to_string('voucher.html', {'ticket': ticket_dict, 'STATIC_URL': settings.BASE_STATIC_PATH})

    buffer = BytesIO()

    HTML(string=html_string).write_pdf(buffer, font_config='/etc/fonts/fonts.conf')

    buffer.seek(0)
    base64_pdf = base64.b64encode(buffer.getvalue()).decode()

    return f"data:application/pdf;base64,{base64_pdf}"


def dia_da_semana(data):
    data_obj = data.date()
    dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    dia_da_semana_idx = data_obj.weekday()

    return dias_da_semana[dia_da_semana_idx]


def QRCode_generate(text):
    try:
        qr = qrcode.QRCode(version=None, box_size=20, border=1, error_correction=qrcode.constants.ERROR_CORRECT_Q)
        qr.add_data(text)
        qr.make()
        img = qr.make_image(fill_color="black", back_color="white")

        with BytesIO() as output:
            img.save(output)
            arr = output.getvalue()

        return f"data:image/png;base64,{base64.b64encode(arr).decode('utf-8')}"
    except Exception as e:
        erro = {
            'caminho': 'inscription > utils > QRCode_generate',
            'mensagem': str(e)
        }
        logger.error('Erro: %r', erro)
        return None


def is_base64(s):
    try:
        base64.decodebytes(s.encode('utf-8'))
        return True
    except TypeError:
        return False
