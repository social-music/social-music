from django.conf.urls import patterns, url
from rango import views
from django.conf.urls.static import static

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^profile/', views.profile, name="profile"),
        url(r'^update-profile/', views.updateProfile, name='update-profile')
        )