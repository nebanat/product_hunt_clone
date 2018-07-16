"""product_hunt URL Configuration

The `urlpatterns` list routes URLs to auth_views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function auth_views
    1. Add an import:  from my_app import auth_views
    2. Add a URL to urlpatterns:  path('', auth_views.home, name='home')
Class-based auth_views
    1. Add an import:  from other_app.auth_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
# from product_hunt.product.views import ProductListView

urlpatterns = [
    # path('', ProductListView.as_view()),
    path('products/', include('product.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'accounts/logout/$', auth_views.LogoutView.as_view(), name='logout')
]
