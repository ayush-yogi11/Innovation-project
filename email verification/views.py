from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import reverse
from .utils import generate_token

def send_verification_email(user, request):
    token = generate_token(user.email)
    verification_link = request.build_absolute_uri(
        reverse('verify_email') + f'?token={token}'
    )
    
    subject = 'Verify your email'
    message = f'Click the link to verify your account: {verification_link}'
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
