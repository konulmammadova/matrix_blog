from django.urls import path
# from rest_framework.routers import DefaultRouter

# from matrix_app.api_views import PostList, PostDetail, UserList, UserDetail, UserPostList, PostViewSet
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('post/detail/<slug:slug>/', views.post_view, name='detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('post/create/', views.post_create_view, name='post_create'),
    path('post/edit/<int:post_id>/', views.post_edit_view, name='post_edit'),
    path('delete/<int:post_id>/', views.delete_view, name='delete'),
    path('edit/profile/', views.edit_profile_view, name='edit_profile'),
    path('authors/<int:author_id>/', views.author_posts_view, name='author_posts'),
    path('my-posts/', views.my_posts_view, name='my_posts'),
    path('activate/<str:token>/', views.activate_account_view, name='activate_account'),
]



# ''' For routing APIViews '''
# urlpatterns += [
#     path('posts/', PostList.as_view(), name='post_list_1'),
#     path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail_1'),
#     path('users/', UserList.as_view(), name='user_list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
#     path('users/<int:pk>/posts', UserPostList.as_view(), name='user_post_list'),
#     # path('users/<int:pk>/posts/<int:pk>/', UserDetail.as_view(), name='user_post_detail'),
#
# ]
#
#
# ''' For Viewset url routing '''
# router = DefaultRouter()
# router.register('posts', PostViewSet, base_name='posts')
#
# urlpatterns += router.urls
