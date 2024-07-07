import smtplib
import os


# function to send ALERT email
def send_email(message):
    try:
        receiver_email_id = "farhad.panahi@gmail.com"
        # to get the password from the environment variable. If not found, use the default value.
        # this is not good practice to store the password in the code. But QPC did not load
        # the environment variable to the container. this is for demo purpose only.
        password = os.getenv("email_password", "hykqfwasddfmhmmh")

        s = smtplib.SMTP("smtp.gmail.com", 587)
        sender_email_id = "semexample1@gmail.com"

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(sender_email_id, password)

        # sending the mail
        s.sendmail(sender_email_id, receiver_email_id, message)

        # terminating the session
        s.quit()
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
