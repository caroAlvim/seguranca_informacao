import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviamsg(numero_aleatorio, endereco_destino):
    server = "smtp.gmail.com"
    port = 587
    username = "xxxxxxxx@gmail.com"
    password = "XXXXXXXXXXXXXXXX"

    mail_from = "xxxxxxxx@gmail.com"
    # mail_to = endereco_destino
    mail_subject = "Código de verificação"
    # mail_body = numero_aleatorio

    mensagem = MIMEMultipart()
    mensagem['From'] = mail_from
    mensagem['To'] = endereco_destino
    mensagem['Subject'] = mail_subject
    mensagem.attach(MIMEText(str(numero_aleatorio), 'plain'))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mensagem)
    connection.quit()