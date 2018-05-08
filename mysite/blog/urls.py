from django.conf.urls import url
from blog import views

app_name='blog'

urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.PostCreateView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete'),
    url(r'^post/draft/$',views.DraftListView.as_view(),name='draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comments_to_post,name='add_comments_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comments_approve,name='comments_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comments_remove,name='comments_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
