from django.urls import path
from engine import views as engine_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', engine_views.landing_page, name='landing'),
    path('module/', engine_views.module_list, name='module-list'),
    path('login/', auth_views.LoginView.as_view(template_name='engine/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
]