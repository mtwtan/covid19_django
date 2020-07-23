from django.urls import path

from . import views

urlpatterns = [
    path('plt_test_view', views.test_view, name='test_view'),
    path('plt_fairfax', views.plt_fairfax_view, name='plt_fairfax_view'),
    path('plt_fairfax_mavg', views.plt_fairfax_movingavg_view, name='plt_fairfax_movingavg'),
    path('', views.index, name='index'),
]

