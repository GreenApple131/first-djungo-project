"""First_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import re_path
from validformapp import validformapp_views
from firstapp import firstapp_views
from authapp import authapp_views

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', firstapp_views.home, name='home'),
    re_path(r'^pizza(?P<pizza_id>\d+)/$', firstapp_views.pizza_detail, name='pizza-detail'),
    re_path(r'^formpage/$', validformapp_views.form_page, name='form-page'),

    re_path(r'^authapp/login/$', auth_views.LoginView.as_view(template_name='authapp/login.html'), name='authapp-login'),
    re_path(r'^authapp/logout/$', auth_views.LogoutView.as_view(next_page='/'), name='authapp-logout'),
    re_path(r'^authapp/$', authapp_views.authapp_home, name='authapp-home'),

    re_path(r'^sign-up/', authapp_views.sign_up, name='sign-up'),
    # re_path(r'^test_app/', include('testurlapp.test_urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
