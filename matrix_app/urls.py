from django.urls import path,include
from . import views
from django.contrib.auth.views import logout
# app_name = 'matrix_app'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('post_create/', views.post_create_view, name='post_create'),
    path('post_edit/<int:post_id>/', views.post_edit_view, name='post_edit'),
    path('delete/<int:post_id>/', views.delete_view, name='delete'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
]
