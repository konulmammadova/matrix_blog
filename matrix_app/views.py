from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from matrix_app.models import Header, Menu, Post, About, SocialMedia, Profile
from matrix_app.forms import ContactForm, LoginForm, RegisterForm, PostForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


base_data = {
    'menus': Menu.objects.all(),
    'social': SocialMedia.objects.all(),
}


# Create your views here.
def index_view(request):
    content = base_data
    content['header'] = Header.objects.first()

    # arr = []

    post_list = Post.objects.filter(status=True)

    # for x in range(400):
        # arr.append(post_list.last())

    paginator = Paginator(post_list, 4)
    page = request.GET.get('page', 1)

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


def about_view(request):
    content = base_data
    about_model = About.objects.first()
    content ['about'] = about_model
    return render(request, 'about.html', content)


def contact_view(request):
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


def post_view(request, post_id):
    content = base_data
    content["post"] = Post.objects.get(id=post_id)
    return render(request, "post.html", content)


def login_view(request):
    content = base_data
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                pass
            # elif user.check_password(password) | user.check_
            elif user and user.is_active:
                login(request, user)
                # profile = Profile.objects.get(user=user)
                # content['posts'] = profile.post_set.all()

                return redirect(reverse('dashboard'))
            else:
                return render(request, 'login.html', content)

    content['login_form'] = login_form
    return render(request, 'login.html', content)


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


def register_view(request):
    content = base_data
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            password = register_form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            # new_user = authenticate(username=user.username, password=password)
            # login(request, new_user)
            return redirect(reverse('login'))
        else:
            content['register_form'] = register_form
            return render(request, 'register.html', content)
    content['register_form'] = register_form
    return render(request, 'register.html', content)


@login_required(login_url='login')
def dashboard_view(request):
    content = base_data
    content['posts'] = Post.objects.filter(author__user=request.user)
    return render(request, 'dashboard.html', content)


@login_required(login_url='login')
def post_edit_view(request, post_id):
    content = base_data
    the_post = Post.objects.get(id=post_id)
    edit_form = PostForm(instance=the_post)
    if request.method == 'POST':
        edit_form = PostForm(request.POST, instance=the_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse('dashboard'))
    content['post'] = the_post
    content['edit_form'] = edit_form
    return render(request, 'post_edit.html', content)


def delete_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='login')
def post_create_view(request):
    content = base_data
    create_form = PostForm()
    if request.method == 'POST':
        # current_user = Profile.objects.filter(user=request.user)[0]
        new_post = Post.objects.create(author=request.user.profile)
        create_form = PostForm(request.POST, instance=new_post)
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse('dashboard'))
    content['create_form'] = create_form
    return render(request, 'post_create.html', content)