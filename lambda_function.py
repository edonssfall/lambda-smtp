import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def lambda_handler(event, context):
    sender = event['sender']
    receiver = event['receiver']
    smtp_server = event['smtp_server']
    smtp_port = event['smtp_port']
    username = event['username']
    password = event['password']

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = event['subject']
    message.attach(MIMEText(event['body'], "plain"))
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(message)

        return {
            'statusCode': 200,
            'body': 'Email sent successfully'
        }
    except smtplib.SMTPException as error:
        return {
            'statusCode': getattr(error, 'smtp_code', -1),
            'body': getattr(error, 'smtp_error', str(error))
        }
