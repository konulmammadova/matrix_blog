from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, UserSerializer
from .models import Post, Profile


'''
GENERAL INFORMATION

There are 4 ways to build API views:
1. Pure Django views
2. APIView subclasses
3. generics.* subclasses
4. viewsets.ModelViewSet

So which one should you use when? My rule of thumb is,

1. Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
2. Use generics.* when you only want to allow some operations on a model
3. Use APIView when you want to completely customize the behaviour.

'''


''' Using APIView '''
class UserList(APIView):
    def get(self, request):
            users = Profile.objects.all()[:10]
            data = UserSerializer(users, many=True).data
            return Response(data)


class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(Profile, pk=pk)
        data = UserSerializer(user).data
        return Response(data)


''' 
Using DRF generic views 

ListCreateAPIView: Allows GET and POST
RetrieveDestroyAPIView: Allows GET and DELETE
'''
class PostList(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Doesnt work !!!
class UserPostList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Post.objects.filter(author_id=self.kwargs['pk'])
        return queryset
    serializer_class = PostSerializer


''' 
Using Viewsets 

With Viewsets we can group views(PostList and PostDetail)
connect them to the urls using routers.
'''
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#


class UserCreate(generics.CreateAPIView):
    # to exempt UserCreate from global authentication scheme.
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
