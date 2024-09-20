"""tutorial URL Configuration

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
from django.urls import path, re_path, include
from .views import home_page, elenca_params, welcome_home, hello_template, hello_params, page_with_static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^$|^/$|^home/$", home_page, name="homepage"),

    path("elencoparametri/", elenca_params, name="params"),
    path("welcome/<str:nome>/<int:eta>/", welcome_home, name="welcome"),

    path("hellotemplate/", hello_template, name="hellotemplate"),

    path("helloparams/<str:nome>/", hello_params, name="param"),

    path("staticelement/", page_with_static, name="static"),

    path('soci/', include('soci.urls')),
]
