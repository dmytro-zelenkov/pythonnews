from django.urls import path
from pnews.views import scrape, news_list, home
from . import views

urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
  path('home', home),
]