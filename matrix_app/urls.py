from django.urls import path
from .views import IndexPageView, AboutPageView, ContactPageView, PostPageView

urlpatterns = [
    path('', IndexPageView, name='index'),
    # path('index', IndexPageView, name='index'),
    path('about/', AboutPageView, name='about'),
    path('contact/', ContactPageView, name='contact'),
    path('post/<int:post_id>/', PostPageView, name='post'),
]
