# pip3 install smtplib
# pip3 install email-to
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText


    


def mail():
    	# The mail addresses and password
	mail_content = " Objek tidak di kenal terdeteksi"
	sender_address = 'projecta082@gmail.com'
	sender_pass = 'Android@123'
	receiver_address = 'yudir413@gmail.com'  # Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	# The subject line#The body and the attachments for the mail
	message['Subject'] = 'ayo lihat siapa itu'
	# Create SMTP session for sending the mail
	message.attach(MIMEText(mail_content, 'plain'))
	session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
	session.starttls()  # enable security
	session.login(sender_address, sender_pass)  # login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')
 
mail()
