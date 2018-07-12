from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Header(models.Model):
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=300)
    bg_image = models.ImageField(default='home-bg.jpg')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = "Әsas Sәhifә"


class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menular"
        ordering = ('order',)



# User = get_user_model()
class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = "Muellif"
        verbose_name_plural = "Muellifler"


class Post(models.Model):
    image = models.ImageField(blank=True, default='post-sample-image.jpg')
    title = models.CharField(max_length=250, db_index=True)
    sub_title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ("-publish_date",)


class SocialMedia(models.Model):
    name = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Sosial sebeke"
        verbose_name_plural = "Sosial Sebekeler"