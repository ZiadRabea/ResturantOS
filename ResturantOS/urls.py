"""
URL configuration for ResturantOS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import *
urlpatterns = [
    path("accounts/", include('Accounts.urls')),
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('error/', error),
    path('products/add', add_product, name="create_product"),
    path('stores/<int:id>', products),
    path('products/<int:id>/delete', delete_product),
    path('products/<int:id>/update', update_product),
    path('products/<int:id>/save', save_product),
    path('products/<int:id>/avtoggle', available_product_toggle),
    path('products/saved', saved_products),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
