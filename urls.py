from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin


landing = lambda request: render(request, "landing.html")

urlpatterns = [
    url(r'^$', landing, name="landing"),
    url(r'^admin/', admin.site.urls),
]
