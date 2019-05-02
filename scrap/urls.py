from django.urls import path
from . import views

app_name = 'scrap'

urlpatterns = [
        path('', views.home, name= 'home'),
        path('data', views.get_data, name='get_data'),
        path('show', views.show_data, name='show'),

]

