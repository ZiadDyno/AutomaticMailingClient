import time
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Setup SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Read credentials
with open("sender_email.txt", "r") as email_file, open("sender_password.txt", "r") as password_file, open("receiver_email.txt", "r") as receiver_file, open("subject_file.txt", "r") as subject_file:
    sender_email = email_file.read().strip()
    sender_password = password_file.read().strip()
    recipients = [email.strip() for email in receiver_file.readlines()]
    subject = subject_file.read().strip()

# Login
server.login(sender_email, sender_password)


for receiver_email in recipients:
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Read the custom body from txt file
    with open('email_body.txt', 'r') as body_file:
        body_content = body_file.read()

    # Define your constant signature
    signature = """
    Best regards,
    Ziad Osama
    Cairo, Egypt
    📞 +20 1080350507
    📧 ziad.elboshy2001@gmail.com
    LinkedIn: https://www.linkedin.com/in/ziad-el-boshy/
    GitHub: https://github.com/ZiadDyno
    """

    # Combine body and signature
    full_body = body_content.strip() + "\n\n" + signature.strip()

    # Attach the final message
    msg.attach(MIMEText(full_body, 'plain'))

    # Add an attachment
    cvpath = 'cv.pdf'

    with open(cvpath, 'rb') as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f'attachment; filename=cv.pdf')
        msg.attach(p)

    # Send the email
    try:
        server.sendmail(sender_email, msg['To'], msg.as_string())
        print(f"✅ Sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send to {receiver_email}: {e}")
        
    time.sleep(5) # wait 5 seconds before sending the next email


server.quit()
