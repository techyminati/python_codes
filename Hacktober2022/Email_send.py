import smtplib

sender_add = "sender69@gmail.com"
receiver_add = "reciver69420@gmail.com"
password = "password"


smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo()  

smtp_server.starttls()  
smtp_server.ehlo() 

smtp_server.login(sender_add, password)

msg_to_be_sent = """
Never gonna ive up,
Never gonna let you down,
Never gonna run around and desert you   
"""


smtp_server.sendmail(sender_add, receiver_add, msg_to_be_sent)
print("Successfully the mail is sent")  

smtp_server.quit()
