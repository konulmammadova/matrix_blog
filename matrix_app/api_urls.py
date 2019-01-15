from django.urls import path
from rest_framework.routers import DefaultRouter
from matrix_app.api_views import PostList, PostDetail, UserList, UserDetail, UserPostList, PostViewSet, UserCreate, \
    LoginView

''' For routing APIViews '''
urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list_1'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail_1'),
    # path('users/', UserList.as_view(), name='user_list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    # path('users/<int:pk>/posts', UserPostList.as_view(), name='user_post_list'),

]

''' For Viewset url routing '''
router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')

urlpatterns += router.urls

urlpatterns = [
    # path('posts/', PostList.as_view(), name='post_list_1'),
    # path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail_1'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='user_login'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    # path('users/<int:pk>/posts', UserPostList.as_view(), name='user_post_list'),
    # path('users/<int:pk>/posts/<int:pk>/', UserDetail.as_view(), name='user_post_detail'),

]
