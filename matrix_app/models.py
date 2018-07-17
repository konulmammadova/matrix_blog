from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.


class Header(models.Model):
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=300)
    bg_image = models.ImageField(default='home-bg.jpg')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = "Әsas Sәhifә"

    def get_bg_image(self):
        if self.bg_image:
            return mark_safe("<img style='width:400px' src='{}' alt=''>".format(self.bg_image.url))


class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Menyu"
        verbose_name_plural = "Menyular"
        ordering = ('order',)


# User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = "Müəllif"
        verbose_name_plural = "Müəlliflər"


class Post(models.Model):
    image = models.ImageField(blank=True, default='post-sample-image.jpg')
    title = models.CharField(max_length=250, db_index=True)
    sub_title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width:200px' src='{}' alt=''>".format(self.image.url))
        else:
            return mark_safe("<img  style='width:200px' src='{}' alt=''>".format(
                "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ("-publish_date",)


class About(models.Model):
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=300)
    bg_image = models.ImageField(default='about-bg.jpg')
    content = models.TextField()

    def get_bg_image(self):
        if self.bg_image:
            return mark_safe("<img style='width:200px' src='{}' alt=''>".format(self.bg_image.url))
        else:
            return mark_safe("<img  style='width:200px' src='{}' alt=''>".format("about-bg.jpg"))

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"


class Contact(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=10, blank=False)
    message = models.TextField(max_length=250, blank=False)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Əlaqə'
        verbose_name_plural = 'Əlaqə'


class SocialMedia(models.Model):
    name = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Sosial şəbəkə"
        verbose_name_plural = "Sosial şəbəkələr"
