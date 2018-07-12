from django.shortcuts import render
from matrix_app.models import Header, Menu, Post, SocialMedia
from matrix_app.forms import ContactForm

base_data = {
    'menus': Menu.objects.all(),
    'social': SocialMedia.objects.all(),
}

# Create your views here.
def IndexPageView(request):
    content = base_data
    content['header'] = Header.objects.first()
    content['posts'] = Post.objects.all()[:4]
    return render(request, 'index.html', content)

def AboutPageView(request):
    content = base_data
    return render(request, 'about.html',content)

def ContactPageView(request):
    content = base_data

    if request.method == 'GET':
        content['form'] = ContactForm()
        return render(request, 'contact.html', content)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.name = form.cleaned_data('name')
            form.email = form.cleaned_data('email')
            form.message = form.cleaned_data('message')
            content['form'] = form
    return render(request, 'contact.html', content)

def PostPageView(request, post_id):
    content = base_data
    content["post"] = Post.objects.get(id=post_id)
    return render(request, "post.html", content)