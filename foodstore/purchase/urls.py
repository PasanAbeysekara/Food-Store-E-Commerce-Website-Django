from django.urls import path
from . import views

app_name = 'purchase'
urlpatterns = [
    path('list/',views.list_view, name='list'),
    path('success/',views.success_view, name='success'),
    path('payment/',views.payment_view, name='payment'),
    path('list/<int:pk>',views.delete_view, name='delete'),
    path("cart/<int:product_id>",views.cart_view,name="cart"),
]
