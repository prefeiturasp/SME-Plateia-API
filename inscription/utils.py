import logging
import base64
import qrcode
from io import BytesIO

logger = logging.getLogger(__name__)


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


def QRCode_generate(width, height, text):
    try:
        qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_Q)
        qr.add_data(text)
        qr.make()
        img = qr.make_image(fill_color="black", back_color="white").resize((width, height))

        with BytesIO() as output:
            img.save(output, format='BMP')
            arr = output.getvalue()

        return f"data:image/png;base64,{base64.b64encode(arr).decode('utf-8')}"
    except Exception as e:
        erro = {
            'caminho': 'inscription > utils > QRCode_generate',
            'mensagem': str(e)
        }
        logger.error('Erro: %r', erro)
        return None
