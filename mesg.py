import smtplib

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login('manjushanamathoti@gmail.com','oolctdtjylfplqsv')
message='I LOVE YOU'
s.sendmail('manjushanamathoti@gmail.com','anithapardhu2000@gmail.com',message)
s.quit()
