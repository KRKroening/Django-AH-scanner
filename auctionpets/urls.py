from django.urls import path

from . import views

app_name = 'auctionpets'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:speciesId>/registerAsCollected/', views.registerAsCollected, name='registerAsCollected'),
]