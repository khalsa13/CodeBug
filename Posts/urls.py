from django.conf.urls import *
from django.contrib import admin
from .views import *
from . import views

urlpatterns = [
    url(r'^create/$',create,name="create"),
    url(r'^(?P<slug>.+)/$', details, name="post_details"),
    url(r'^$', feed_home, name="feedHome"),

]