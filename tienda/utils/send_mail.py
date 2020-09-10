# -*- coding: utf-8 -*-

from tienda.utils import constantes
import base64
import smtplib
import ssl


def get_correo(receiver_email, message=False):
    if message:
        try:
            port = 465  # For SSL
            smtp_server = "cualquier.servidor.smpt"
            sender_mail = "orders@bernini.com"
            message = str.encode(message, "utf-8")  # codificar en UTF-8
            context = ssl.create_default_context()
            v_secret_pass = base64.b64decode(constantes.EMAIL_PASS)
            with smtplib.SMTP_SSL(smtp_server,
                                  port, context=context) as server:
                server.login(sender_mail, v_secret_pass.decode('utf-8'))
                server.sendmail(receiver_email, sender_mail,
                                message)
                return {'result': 'Your order was sent to Bernini, thank you.',
                        'status_code': 201}
        except Exception as e:
            print(str(e))
            return {'result': 'Error when send message',
                    'status_code': 500}
