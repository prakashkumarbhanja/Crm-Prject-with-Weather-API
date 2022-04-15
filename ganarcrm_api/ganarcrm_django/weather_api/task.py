from celery import shared_task

from django.core.mail import send_mail

@shared_task(name='send_weather_data_by_mail')
def send_weather_api_mail(subject,from_email,message, to_email ):
    
    send_mail(subject, message, from_email, [to_email], fail_silently = False)
    
    return "Mail Sent!!!"
