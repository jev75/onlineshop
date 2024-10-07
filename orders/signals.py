from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Order

# Funkcija, kuri siunčia pranešimą apie naują užsakymą
@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:
        # Sukuriamas el. laiško pavadinimas
        subject = f'Naujas užsakymas Nr. {instance.id}'
        # Sukuriamas HTML formato el. laiškas
        html_message = render_to_string('orders/order_notification_email.html', {'order': instance})
        # HTML formato el. laiškas konvertuojamas į paprastą tekstą
        plain_message = strip_tags(html_message)
        # Siuntėjo el. pašto adresas
        from_email = 'your_email@example.com'
        # Gavėjo el. pašto adresas
        to = 'yourMail@gmail.com'  # jūsų el. pašto adresas

        # Siunčiamas el. laiškas
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)