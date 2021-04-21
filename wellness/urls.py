from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:pk>', views.postact, name='postact'),
    path('editpost/<int:act_id>', views.editpost, name='editpost')
]