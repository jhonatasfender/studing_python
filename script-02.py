# import re,email,smtplib
# from lib.xlrd import xlrd

# # msg = email.message_from_string('warning')
# # msg['From'] = "debora.turibio@hotmail.com"
# # msg['To'] = "jhonatas.fender@gmail.com"
# # msg['Subject'] = "helOoooOo"

# msg = '''\
# From: debora.turibio@hotmail.com
# To: jhonatas.fender@gmail.com
# Subject: testin'...

# This is a test '''

# s = smtplib.SMTP("smtp.live.com",587)
# s.ehlo() 
# s.starttls() 
# s.ehlo()
# s.login('debora.turibio@hotmail.com', 'mecatual2012')

# s.sendmail("debora.turibio@hotmail.com", "jhonatas.fender@gmail.com", msg)

# s.quit()

import email,smtplib,re,os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from lib.xlrd import xlrd


def send_mail(send_from, send_to, subject, text, files=None,server="smtp.live.com"):
    # assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in os.walk(files) or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

	smtp = smtplib.SMTP("smtp.live.com",587)
	smtp.ehlo() 
	smtp.starttls() 
	smtp.ehlo()
	smtp.login('debora.turibio@hotmail.com', 'mecatual2012')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

w = xlrd.open_workbook("/home/jonatas/Desktop/email.xlsx")
s = w.sheet_by_index(0);
a = list();
for r in range(s.nrows):
	c = s.row_values(r)

	if(re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",c[1])):
		print(c[1])
		a.append(c[1])
		send_mail("debora.turibio@hotmail.com",c[1],"Curriculo Vitale","Boa noite ou bom dia","/home/jonatas/Downloads/debora.pdf")


