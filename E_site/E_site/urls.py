"""
URL configuration for E_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from . import views
from adminapp import views
from .import settings
from django.contrib.staticfiles.urls import static 


# using django TemplateView to render (replacing views)
from django.views.generic import TemplateView


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.index_page, name = "home" ),
#     path("about/", views.about_page, name = 'about'),
#     path("shop/", views.shop_page, name = 'shop-single'),
#     path("contact", views.contact_page, name='contact'),    
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name = "home"),
    # path('', TemplateView.as_view(template_name ="index.html"), name = "home"),
    path('about/', TemplateView.as_view(template_name="about.html"), name = 'about'),
    path("shopSingle/", TemplateView.as_view(template_name="shop-single.html"), name = 'shop-single'),
    path("contact/", TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('shop/', TemplateView.as_view(template_name="shop.html"), name='shop'),
    
    path('',include("adminapp.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
