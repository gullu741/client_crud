#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'clients'

urlpatterns = [
    # Create a client
    path('create/', views.ClientCreateView.as_view(), name='client_create'),
    # Retrieve client list
    path('', views.ClientListView.as_view(), name='client_list'),
    # Retrieve single client object
    re_path(r'^(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='client_detail'),
    # Update a client
    re_path(r'^(?P<pk>\d+)/update/$', views.ClientUpdateView.as_view(), name='client_update'),
    # Delete a client
    re_path(r'^(?P<pk>\d+)/delete/$', views.ClientDeleteView.as_view(), name='client_delete')

    # # Create a client
    # path('create/', views.client_create, name='client_create'),
    # # Retrieve client list
    # path('', views.client_list, name='client_list'),
    # # Retrieve single client object
    # re_path(r'^(?P<pk>\d+)/$', views.client_detail, name='client_detail'),
    # # Update a client
    # re_path(r'^(?P<pk>\d+)/update/$', views.client_update, name='client_update'),
    # # Delete a client
    # re_path(r'^(?P<pk>\d+)/delete/$', views.client_delete, name='client_delete'),

]