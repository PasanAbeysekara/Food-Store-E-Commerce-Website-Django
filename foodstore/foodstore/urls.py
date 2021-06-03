from django.contrib import admin
from django.urls import path, include
from products import views as products_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_views.home_view),
    path('products/', include('products.urls')),
    path('purchase/', include('purchase.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()