from django.contrib.auth.views import LoginView
from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('profile/', views.profile, name='profile')
]
