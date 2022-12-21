# from django.shortcuts import render
# from Email_template.settings import EMAIL_HOST_USER

# # Create your views here.
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags





# def send_mails(request):
#     if request.method == 'POST':
#             email = request.POST.get('email')
#             subject = request.POST.get('subject')
#             content = request.POST.get('content')
#             html = request.POST.get('html')
#             Msg = EmailMultiAlternatives(f'{subject}',f'{content}',EMAIL_HOST_USER,[f'{email}'])
#             Msg.attach_alternative(html,"text/html")
#             Msg.send()
#             return render(request, 'myapp/Email_template.html')

#     else:
#         return render(request, 'myapp/Email_template.html')


        


# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'sohailbadeghar561@gmail.com',
#     ['sohailbadeghar561@gmail.com'],
#     fail_silently=False,
# )


import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("sohailbadeghar561@gmail.com")  # Change to your verified sender
to_email = To("sohailbadeghar561@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)



