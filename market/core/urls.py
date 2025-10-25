from django.contrib.auth import views as auth_views #we change the name because otherwise it clash with views 
from django.urls import path 

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
    path("feedback/", views.review, name="review"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
]


