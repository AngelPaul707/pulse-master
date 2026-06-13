import os
import smtplib

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

subject = "Daily Pulse Report"
body = "Good Morning! This email was sent automatically by Pulse MasterKit."

message = f"Subject: {subject}\n\n{body}"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(
        EMAIL_USER,
        EMAIL_TO,
        message
    )

print("Email sent successfully!")
