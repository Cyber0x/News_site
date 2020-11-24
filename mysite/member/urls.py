from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('registration/', views.RegisterUserView.as_view(), name='registration'),
    path('login', views.BlogLoginView.as_view(), name='login'),
    path('logout', views.LogoutUserView.as_view(), name='logout'),

]