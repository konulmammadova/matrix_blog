from django.core.management import BaseCommand

from matrix_app.models import Post


class Command(BaseCommand):
    help= "Create slug for all posts"

    def handle(self, *args, **kwargs):
        print("Started to create slugs...")
        posts = Post.objects.all()

        for post in posts:
            if not post.slug:
                post.save()
                print('{}'.format(post.slug))

        print('Completed...')