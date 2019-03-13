from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.officer_list, name='officer_list'),
#    url(r'^$', views.underconstruction, name='under_construction'),
]
