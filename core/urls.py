from django.urls import path
from . import views

# massage
from .views import  CreateThread, ListThreads, ThreadView, CreateMessage


urlpatterns = [
    path('',views.index, name='index'),
    path('settings', views.setting, name = 'settings'),
    path('upload', views.upload, name = 'upload'),
    path('follow', views.follow, name = 'follow'),
    path('search', views.search, name = 'search'),
    path('like-post', views.like_post, name = 'like-post'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
]