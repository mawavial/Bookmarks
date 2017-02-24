"""Define bkm_app urls pattern"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    #Show all of some user's bookmarks
    url(r'^bookmarks/$', views.bookmarks, name='bookmarks'),
    #Page that renders details on a bookmark
    url(r'^bookmarks/(?P<bookmark_id>\d+)/$', views.bookmark, name='bookmark'),
    #Page in which an user can add a bookmark
    url(r'^new_bookmark/$', views.new_bookmark, name='new_bookmark'),
    #Page for bookmark edition
    url(r'edit_bookmark/(?P<bookmark_id>\d+)/$', views.edit_bookmark, name='edit_bookmark'),
    
    
]
