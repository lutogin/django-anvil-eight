from ..settings import pizza_settings
import smtplib
import email.message


def send_mail(email_to, body):
    """Отправка письма"""
    """Подготовим тело сообщения"""
    msg = email.message.Message()
    msg['Subject'] = 'Заказ принят'
    msg['To'] = email_to
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    """Подготовим сервер для отправки"""
    smtp_server = smtplib.SMTP(pizza_settings['smtp']['server'], pizza_settings['smtp']['port'])
    # smtp_server.connect()
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo()
    smtp_server.login(pizza_settings['smtp']['user'], pizza_settings['smtp']['password'])
    smtp_server.sendmail(pizza_settings['from'], [msg['To']], msg.as_string().encode('utf8'))
    smtp_server.quit()
