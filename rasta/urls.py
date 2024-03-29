"""rasta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('frequency/', include('frequencyWorkshop.urls')),
    path('image/', include('imageWorkshop.urls')),
    path('',include('TeamData.urls')),
    path('city/', include('citygame.urls')),
    path('source_coding/', include('source_coding_image_split.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
