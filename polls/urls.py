from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(),
        name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.deletepoll, name='deletepoll'),
    url(r'^(?P<question_id>[0-9]+)/addpost/$', views.addpost, name='addpost'),
    url(r'^addpoll/$', views.addpoll, name='addpoll'),
    url(r'^(?P<question_id>[0-9]+)/deletepost/(?P<post_id>[0-9]+)/$',
        views.deletepost, name='deletepost'),
    url(r'^(?P<question_id>[0-9]+)/editpost/(?P<post_id>[0-9]+)/$',
        views.editpost, name='editpost'),
]
