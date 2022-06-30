"""hello URL Configuration
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
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, create_sketchpad, sketchpad_view, update_sketchpad, delete_sketchpad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('sketch/<int:pk>/', sketchpad_view, name="sketchpad_view"),
    path('sketch/add/', create_sketchpad, name="create_sketchpad"),
    path('sketch/<int:pk>/update', update_sketchpad, name="update_sketchpad"),
    path('sketch/<int:pk>/delete', delete_sketchpad, name="delete_sketchpad"),
]
