from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^$', Home, name="Home"),
    url(r'^PersonalDetails/$', Detail, name="createAcc"),
    url(r'^SignUp/$', register_user, name="signup"),
    url(r'^CodeBug/$', page1, name="CodeBug"),

]
