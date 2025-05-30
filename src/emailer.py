import smtplib
import time
import csv
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import re

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))


def send_emails(mode, csv_path, cv_path, sender_email, sender_password, signature, subject=None, body=None):
    results = []
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender_email, sender_password)
    except Exception as e:
        print("✖️ Login failed:", str(e))
        return []

    with open(csv_path, newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            email = row['email'].strip()
            #! Validate each email before trying to send
            if not is_valid_email(email):
                print(f"❌ Invalid email format: {email}")
                results.append((email, False))
                continue
            
            actual_subject = subject or row.get('subject', '').strip()
            actual_body = body or row.get('body', '').strip()
            full_body = actual_body + "\n\n" + signature

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = actual_subject
            msg.attach(MIMEText(full_body, 'plain'))

            with open(cv_path, 'rb') as cv_file:
                p = MIMEBase('application', 'octet-stream')
                p.set_payload(cv_file.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', 'attachment; filename=CV.pdf')
                msg.attach(p)

            try:
                server.sendmail(sender_email, email, msg.as_string())
                print(f"✅ Sent to {email}")
                results.append((email, True))
            except Exception as e:
                print(f"❌ Failed to send to {email}: {e}")
                results.append((email, False))

            time.sleep(2)
    server.quit()
    return results
