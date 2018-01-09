# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import email,smtplib,re,os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from lib.xlrd import xlrd


smtp = smtplib.SMTP("smtp.live.com",587)
smtp.ehlo() 
smtp.starttls() 
smtp.ehlo()
smtp.login('debora.turibio@hotmail.com', 'mecatual2012')

def send_mail(send_from, send_to, subject, text, files=None,server="smtp.live.com"):
    # assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = unicode(subject, 'utf-8')

    msg.attach(MIMEText(text))

    with open(files, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(files)
        )

    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(files)
    msg.attach(part)


    smtp.sendmail(send_from, send_to, msg.as_string())
    # smtp.quit()

w = xlrd.open_workbook("/home/jonatas/Desktop/email.xlsx")
s = w.sheet_by_index(0);

for r in range(s.nrows):
	c = s.row_values(r)

	if(re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",c[1])):
		print(c[1])
		send_mail(
			"debora.turibio@hotmail.com",
			c[1],
			"Currículo estudante de enfermagem",
			'Sou Débora de Andrade Turíbio, estudante de enfermagem cursando o quinto semestre. Desejo adquirir experiência e oportunidade para poder entrar no mercado de trabalho da saúde, alcançando os objetivos profissionais.',
			"./debora.pdf"
		)


