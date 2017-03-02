from django.conf.urls import url

from . import views

app_name = 'contactsapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addContact/$', views.AddContactView.as_view(), name='addContact'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^postContact/$', views.postContact, name='postContact'),
]
