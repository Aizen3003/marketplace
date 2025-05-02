"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from marketplace import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('towarlist/', views.towar_list, name='towar_list'),
    path('towar/<int:id>/', views.towar, name='towar'),
    path('cart/', views.cart, name='cart'),
    path('accounts/login/', views.login_polso, name='login'),
    path('logout/', views.logout_polso, name='logout'),
    path('regist/', views.regist, name='regist'),
    path('dobawtowar/', views.dobaw_towar, name='dobawtowar'),
    path('delete/', views.delete, name='delete'),
    path('plus/', views.plus, name='plus'),
    path('minus/', views.minus, name='minus'),
    path('corect/', views.corect, name='corect')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)