from django.shortcuts import render, redirect
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

    # arr = []

    post_list = Post.objects.all()

    # for x in range(400):
        # arr.append(post_list.last())

    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    if page:
        posts = paginator.get_page(page)
    else:
        posts = paginator.get_page(1)
    max_index = len(paginator.page_range)
    index = int(page) - 1
    start_index = index - 5 if index > 5 else 0
    end_index = index + 5 if index <= max_index else max_index - 1
    content['page_index'] = paginator.page_range[start_index:end_index]
    content['posts'] = posts

    return render(request, 'index.html', content)


def AboutPageView(request):
    content = base_data
    about_model = About.objects.first()
    content ['about'] = about_model
    return render(request, 'about.html', content)


def ContactPageView(request):
    content = base_data
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajiniz ugurla gonderildi. Tesekkur edirik!")
            return redirect('contact')
        else:
            content['form'] = form
            return render(request, 'contact.html', content)
    else:
        content['form'] = form
        return render(request, 'contact.html', content)


def PostPageView(request, post_id):
    content = base_data
    content["post"] = Post.objects.get(id=post_id)
    return render(request, "post.html", content)
