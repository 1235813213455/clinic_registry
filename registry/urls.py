from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^registry/$', views.index, name='index'),
    url(r'^registry/(?P<doctor_id>[0-9]+)/$', views.doctor, name='doctor'),
    url(r'^registry/register$', views.register, name='register'),
    url(r'^registry/time_occupied_error/', views.time_occupied, name='time_occupied')
]
