from django.conf.urls import url
from .api import CustomerApi

urlpatterns = [
    url(r'^customers$', CustomerApi.as_view())
]