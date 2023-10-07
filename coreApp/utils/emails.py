from django.conf import settings
from django.core.mail import send_mail








def sendSignupEmail(user):
    subject = 'Welcome to BeeMindful-Buzz'
    message = f'Hi {user.username}, thank you for registering for BeeMindful-Buzz. I am the owner and creator Melissa. This project has been a passion of mine for some time now I can not wait to get to know you! Please feel free to reach out if you have any questions'
    email_from = settings.EMAIL_HOST_ALT_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )