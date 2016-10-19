from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^state/(?P<state>\w+)/', views.state, name='state'),
        url(r'^member/(?P<govtrack_id>\w+)', views.congress_person, name='congress_person'),
        url(r'^locate/', views.ajax_locate_district, name='locate'),
]
