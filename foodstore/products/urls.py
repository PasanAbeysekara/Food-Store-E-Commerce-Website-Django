from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.home_view ,name ='home'),
    path('create/',views.create_view, name='create'),
    path('detail/<int:pk>',views.detail_view, name='detail'),
    path('delete/<int:pk>',views.delete_view, name='delete')
]