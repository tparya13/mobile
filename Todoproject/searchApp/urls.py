from django.urls import path
from . import views
app_name='searchApp'
urlpatterns = [
    path('',views.searchproduct,name='searchproduct'),
]