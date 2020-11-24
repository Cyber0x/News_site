from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('search', views.SearchResultView.as_view(), name='search_results'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete'),
]