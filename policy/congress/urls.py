from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^state/(?P<state>\w+)/', views.state, name='state'),
        url(r'^member/(?P<govtrack_id>[0-9]+)', views.congress_person, name='congress_person'),
        url(r'^locate/', views.ajax_locate_district, name='locate'),
        url(r'^my_district/(?P<state>\w+)/(?P<district>[0-9]{2})', views.my_district, name='my_district'),
]
