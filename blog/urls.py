from django.conf.urls import include, url
from . import views
urlpatterns = [
    # blog
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^blog/drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^blog/post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^blog/post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^blog/post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^blog/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^blog/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

    # info
    url(r'^$', views.home, name='home'),
    url(r'^info/$', views.info, name='info'),
    url(r'^home/$', views.home, name='home'),


    url(r'^exhibit/image$', views.exhibit_image, name='exhibit_image'),

    # guestbook
    url(r'^guestbook/$', views.guestbook_list, name='guestbook_list'),
]