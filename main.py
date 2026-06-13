import os
import smtplib

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

if not EMAIL_USER:
    raise Exception("EMAIL_USER secret is missing")

if not EMAIL_PASS:
    raise Exception("EMAIL_PASS secret is missing")

if not EMAIL_TO:
    raise Exception("EMAIL_TO secret is missing")

subject = "Daily Pulse Report"
body = """
Good Morning!

This email was sent automatically by Pulse MasterKit using GitHub Actions.

Have a great day!
"""

message = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(
            EMAIL_USER,
            EMAIL_TO,
            message
        )

    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")
    raise
