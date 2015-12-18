__author__ = 'cleytonpedroza'

import mimetypes
import os
import smtplib

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def adiciona_anexo(msg, filename):
    if not os.path.isfile(filename):
        return

    ctype, encoding = mimetypes.guess_type(filename)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    maintype, subtype = ctype.split('/', 1)

    if maintype == 'text':
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)
    elif maintype == 'image':
        with open(filename, 'rb') as f:
            mime = MIMEImage(f.read(), _subtype=subtype)
    elif maintype == 'audio':
        with open(filename, 'rb') as f:
            mime = MIMEAudio(f.read(), _subtype=subtype)
    else:
        with open(filename, 'rb') as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())

        encoders.encode_base64(mime)

    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mime)

de = 'monitor.m2m@gmail.com'
para = ['cleytonpedroza@gmail.com', 'mudrik@gmail.com']

msg = MIMEMultipart()
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = 'REDE 001'

# Corpo da mensagem
msg.attach(MIMEText('Exemplo de email HTML com anexo do &lt;b&gt;Buteco Open Source&lt;b/&gt;.', 'html', 'utf-8'))

# Arquivos anexos.
adiciona_anexo(msg, './users.csv')

raw = msg.as_string()

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('monitor.m2m@gmail.com', 'Monitor_m2m') # email, senha
smtp.sendmail(de, para, raw)
smtp.quit()