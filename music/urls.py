from django.urls import path
from .views import ListSongsView
from . import views


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('post/', views.ListSongsView, name='post'),
]