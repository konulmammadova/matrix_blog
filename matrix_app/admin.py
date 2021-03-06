from django.contrib import admin
from matrix_app.models import Header, Menu, About, Post, SocialMedia, Contact, Profile, Token


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'get_bg_image')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'get_bg_image')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'slug', 'title', 'sub_title', 'author', 'publish_date')


admin.site.register(Profile)


@admin.register(SocialMedia)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
