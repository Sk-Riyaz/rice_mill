from django.conf.urls import url, include
from . import views as mill_views
from django.contrib.auth import views as auth_views

app_name = 'rice_mill'

urlpatterns = [
      url(r'^index/$', mill_views.landing, name='index'),
      url(r'^sub/$', mill_views.submit, name='submit'),
      url(r'^login/$', auth_views.login, name='login' ),
      #url('^', include('django.contrib.auth.urls')),
      ]
