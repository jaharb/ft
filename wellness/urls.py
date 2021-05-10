from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:act_id>', views.postact, name='postact'),
    path('editpost/<int:act_id>', views.editpost, name='editpost'),
    path('accounts/', include('django.contrib.auth.urls'))
]