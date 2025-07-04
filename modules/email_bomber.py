import smtplib
from email.message import EmailMessage

def send_emails(target_email, count):
    success = 0
    try:
        for _ in range(count):
            msg = EmailMessage()
            msg.set_content("This is a test message from BUGZKINGZ.")
            msg["Subject"] = "💣 You’ve been bombed"
            msg["From"] = "example@example.com"
            msg["To"] = target_email
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login("example@example.com", "password")  # Replace w/ real creds
                smtp.send_message(msg)
                success += 1
    except Exception as e:
        return f"Failed after {success} emails. Error: {e}"
    return f"Successfully sent {success} emails."
