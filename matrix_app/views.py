from django.shortcuts import render
from matrix_app.models import Header, Menu, Post, About, SocialMedia
from matrix_app.forms import ContactForm
from django.core.paginator import Paginator
from django.contrib import messages

base_data = {
    'menus': Menu.objects.all(),
    'social': SocialMedia.objects.all(),
}


# Create your views here.
def IndexPageView(request):
    content = base_data
    content['header'] = Header.objects.first()

    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    if page:
        posts = paginator.get_page(page)
    else:
        posts = paginator.get_page(1)

    content['posts'] = posts

    return render(request, 'index.html', content)


def AboutPageView(request):
    content = base_data
    about_model = About.objects.first()
    content ['about'] = about_model
    return render(request, 'about.html', content)


def ContactPageView(request):
    content = base_data
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajiniz ugurla gonderildi. Tesekkur edirik!")

    form = ContactForm()
    content['form'] = form
    return render(request, 'contact.html', content)


def PostPageView(request, post_id):
    content = base_data
    content["post"] = Post.objects.get(id=post_id)
    return render(request, "post.html", content)
