import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# 邮件发送者和接收者的邮箱地址
sender = 'sender@example.com'
recipient = 'recipient@example.com'

# 创建邮件对象并设置邮件头部
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = '邮件主题'

# 添加邮件正文
body = '这是一封测试邮件，请勿回复。'
msg.attach(MIMEText(body, 'plain'))

# 添加图片附件
with open('image.jpg', 'rb') as f:
    img_data = f.read()
img = MIMEImage(img_data, name='image.jpg')
msg.attach(img)

# 添加普通附件
filename = 'document.pdf'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

# 连接SMTP服务器并发送邮件
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login(sender, 'password')
text = msg.as_string()
server.sendmail(sender, recipient, text)
server.quit()
