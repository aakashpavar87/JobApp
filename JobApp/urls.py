"""
URL configuration for JobApp project.

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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.http import HttpResponseNotFound
from django.urls import path, include

def not_found(request, **kwargs):
    return HttpResponseNotFound("Not Found none Error Code : 404")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('subscribe.urls')),
    path('uploads/', include('uploadapp.urls')),
    # path('<path:invalid_path>', not_found),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [path('<path:invalid_path>', not_found),]
