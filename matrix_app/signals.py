from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from matrix_app.models import Profile

# User = get_user_model()


@receiver(post_save, sender=User, dispatch_uid='create_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=User, dispatch_uid='save_user_profile')
# def save_user_profile(sender, instance, **kwargs):
#     instance.save()
