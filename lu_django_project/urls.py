"""lu_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import lu_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hello', lu_app.views.show_hello),
    path('show_html', lu_app.views.show_html),
    path('get_time', lu_app.views.get_time),
    path('enter_name', lu_app.views.enter_name),
    path('university', lu_app.views.university),
    path('add_post', lu_app.views.add_post),
    path('', lu_app.views.get_all_posts),
    path('get_post/<int:post_id>', lu_app.views.get_post),
]

