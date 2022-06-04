from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=get_user_model())
def make_token_user(sender, instanse, create=False, **kwargs):
    if create:
        Token.objects.create(user=instanse)
