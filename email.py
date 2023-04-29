import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login('manjushanamathoti@gmail.com','oolctdtjylfplqsv')
message='Hello Sister I LOVE YOU'
s.sendmail('manjushanamathoti@gmail.com','prathyushanamathoyi55@gmail.com',message)
s.quit()
