"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("createpage",creatpage),
    path("detail/<int:id>",detaillpage,name="detailpage"),
    path("delete/<int:id>",delete),
    path("edit/<int:id>",edit),
    path("createuser",createuser),
    path('login',userlogin),
    path('logout/',userlogout),
    path("profile",userprofile),
    path("booknow/<int:id>/",booknow),
    path("addroom/<int:id>",roomadd),
    path("chooseroom/<int:id>/",chooseroom),
    path('room/add/<int:id>/', roomadd, name='roomadd'),
    path('editroom/<int:id>/',editroom),
    path('delroom/<int:id>/',delroom)
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
