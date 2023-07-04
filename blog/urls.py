from django.urls import re_path, include
from django.contrib import admin
from . import views

urlpatterns = [
    re_path("admin/", admin.site.urls),
    re_path("accounts/", include("django.contrib.auth.urls")),
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')

]