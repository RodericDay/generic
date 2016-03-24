from django.http import HttpResponse
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', lambda request: HttpResponse("Hello"), name="landing"),
    url(r'^admin/', admin.site.urls),
]
