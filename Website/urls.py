from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^atualizarperfil/$', views.atualizarperfil, name='atualizarperfil'),
    ]