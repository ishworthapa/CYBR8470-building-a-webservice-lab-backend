from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt
from . import views
#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^session', csrf_exempt(controllers.Session.as_view())),
    url(r'^register', csrf_exempt(controllers.Register.as_view())),
    url(r'^events', csrf_exempt(controllers.Events.as_view())),
    url(r'^activateifttt', csrf_exempt(controllers.ActivateIFTTT.as_view())),
    url(r'^dogs/(?P<pk>[0-9]+)$', views.DogDetail.as_view()),
    url(r'^dogs/$', views.DogList.as_view()),
    url(r'^breeds/(?P<pk>[0-9]+)$', views.BreedDetail.as_view()),
    url(r'^breeds/$', views.BreedList.as_view()),
    url(r'^', include(router.urls)),
]
