from django.contrib import admin
from matrix_app.models import Header, Menu, Author, Post, SocialMedia

# Register your models here.


# class AuthorAdmin(admin.ModelAdmin):
#     list_display = (author.user.first_name, author.user.last_name)

admin.site.register(Header)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Menu)
admin.site.register(SocialMedia)