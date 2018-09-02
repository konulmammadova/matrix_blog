import random, string

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
User = get_user_model()


class Header(models.Model):
    title = models.CharField(max_length=225)
    sub_title = models.CharField(max_length=300)
    bg_image = models.ImageField(default='home-bg.jpg')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = "Әsas Sәhifә"
        verbose_name_plural = "Әsas Sәhifә"

    def get_bg_image(self):
        if self.bg_image:
            return mark_safe("<img style='width:250px' src='{}' alt=''>".format(self.bg_image.url))


class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Menyu"
        verbose_name_plural = "Menyu"
        ordering = ('order',)


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
    name = models.CharField(max_length=150, verbose_name="Ad")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=10, verbose_name="Telefon")
    message = models.TextField(max_length=250, verbose_name="Mesaj")

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    picture = models.ImageField(default='about-bg.jpg', upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = "Müəllif"
        verbose_name_plural = "Müəlliflər"


class Post(models.Model):
    image = models.ImageField(blank=True, default='default-profile.jpg')
    title = models.CharField(max_length=250, db_index=True)
    sub_title = models.CharField(max_length=250)
    content = RichTextUploadingField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    publish_date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.title_cache = self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

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


class Token(models.Model):
    def random_token_generator(size=20, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default=random_token_generator())
    activation = models.BooleanField(default=False)


