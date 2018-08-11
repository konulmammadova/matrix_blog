from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from matrix_app.models import Profile, Post
from matrix_app.helper import slugify


@receiver(post_save, sender=User, dispatch_uid='signal_create_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=Post, dispatch_uid='signal_create_slug')
def signal_create_slug(*args, **kwargs):

    # def create_slug(inst, new_slug=None):
    #     slug = slugify(inst.title)
    #     qs = Post.objects.filter(slug=slug)
    #     if qs.exists():
    #         new_slug = slugify("{} {}".format(inst.title, qs.first().id))
    #         return create_slug(inst, new_slug=new_slug)
    #
    #     return slug

    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()

    # else:
    #     instance.slug = create_slug(instance.title)
    #     instance.save()
        # pass
