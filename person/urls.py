from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^blogs/$', views.blog, name="blog"),
    url(r'^pizzas/$', views.pizza, name="pizza"),
    url(r'^pizzas/(?P<id>\d+)/$', views.pizza_details, name="pizza_detail"),
]
