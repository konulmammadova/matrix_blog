from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404

from matrix_app.models import Header, Menu, Post, About, SocialMedia, Profile, Token
from matrix_app.forms import ContactForm, LoginForm, RegisterForm, PostForm, UserForm, ProfileForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse
from django.conf import settings

User = get_user_model()

base_data = {
    'menus': Menu.objects.all(),
    'social': SocialMedia.objects.all(),
}


def index_view(request):
    content = base_data
    content['header'] = Header.objects.first()

    post_list = Post.objects.filter(status=True)

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
    content['about'] = about_model
    return render(request, 'about.html', content)


def contact_view(request):
    content = base_data
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mesajınız uğurla göndərildi. Təşəkkür edirik!")
            return redirect('contact')
        else:
            content['form'] = form
            return render(request, 'contact.html', content)
    else:
        content['form'] = form
        return render(request, 'contact.html', content)


def post_view(request, slug):
    content = base_data
    content["post"] = Post.objects.get(slug=slug)
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
            if user and user.is_active:
                if hasattr(user, 'token'):
                    if user.token.activation:
                        login(request, user)
                        return redirect(reverse('dashboard'))
                    else:
                        messages.success(request, 'Hesabınızı aktivləşdirmək üçün mailinizi yoxlayın.')
                        return redirect(reverse('login'))
                login(request, user)
                return redirect(reverse('dashboard'))
            else:
                messages.warning(request, 'Məlumatlarınızı düzgün daxil edin.')
                return redirect(reverse('login'))

    content['login_form'] = login_form
    return render(request, 'login.html', content)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


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
            token = Token.objects.create(user=user)
            url = 'http://' + request.get_host() + '/activate/' + token.name
            subject, from_email, to = 'Matrix Activation email', settings.EMAIL_HOST_USER, register_form.cleaned_data.get(
                'email')
            text_content = 'Thank you for registration'
            html_content = "<p><a href='" + url + "'>Please activate your account</a></p>"
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, "Aktivasiya mailiniz uğurla göndərildi. Zəhmət olmasa mailinizi yoxlayın.")

            return redirect(reverse('login'))
        else:
            messages.error(request, "Məlumatlarınız keçərli deyil. Zəhmət olmasa yenidən daxil edin.")
            content['register_form'] = register_form
            return render(request, 'register.html', content)
    content['register_form'] = register_form
    return render(request, 'register.html', content)


def activate_account_view(request, token):
    content = base_data
    user_token = Token.objects.filter(name=token)[0]
    if not user_token.activation:
        user_token.activation = True
        user_token.save()
        messages.success(request, 'Hesabınız uğurla aktivləşdirildi.Zəhmət olmasa daxil olun.')
        return redirect(reverse('login'))
    else:
        return redirect(reverse('index'))


@login_required(login_url='login')
def dashboard_view(request):
    content = base_data
    content['posts'] = Post.objects.filter(author__user=request.user)

    post_list = Post.objects.filter(author__user=request.user)

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
    return render(request, 'dashboard.html', content)


@login_required(login_url='login')
def post_create_view(request):
    content = base_data
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user.profile
            post.save()
            return redirect(reverse('dashboard'))
    content['form'] = form
    content['type'] = 'create'
    return render(request, 'post_form.html', content)


@login_required(login_url='login')
def post_edit_view(request, post_id):
    content = base_data
    the_post = get_object_or_404(Post, id=post_id)
    form = PostForm(instance=the_post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=the_post)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))
    content['form'] = form
    content['type'] = 'edit'
    return render(request, 'post_form.html', content)


@login_required(login_url='login')
def delete_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='login')
def edit_profile_view(request):
    content = base_data
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user_form.save()
            profile.save()
            messages.success(request, 'Məlumatlarınız müvəfəqiyyətlə yeniləndi!')
            return redirect(reverse('edit_profile'))

    content['user_form'] = user_form
    content['profile_form'] = profile_form
    return render(request, 'edit_profile.html', content)


@login_required(login_url='login')
def my_posts_view(request):
    content = base_data
    post_list = Post.objects.filter(author=request.user.profile)

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

    return render(request, 'my_posts.html', content)


def author_posts_view(request, author_id):
    content = base_data
    author = get_object_or_404(Profile, pk=author_id)
    post_list = Post.objects.filter(author_id=author_id)

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
    content['author'] = author

    return render(request, 'author_posts.html', content)
