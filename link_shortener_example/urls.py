"""link_shortener_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from links.views import link_creator, link_redirector, link_list, check_admin

urlpatterns = [
    path('admin/admin', admin.site.urls),
    path('admin/check', check_admin, name='admin-checker'),
    path('', link_creator, name='creator'),
    path('<str:link_code>', link_redirector, name='redirect'),
    path('show/urls', link_list, name='links')
]
