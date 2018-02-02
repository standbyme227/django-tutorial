from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path(r'^$',views.index, name='index'),
    path(r'^(?P<question_id>\d+)/$',views.detail, name='detail'),
    path(r'^(?P<question_id>\d+)/results/$',views.results, name='results'),
    path(r'^(?P(question_id>\d+)/vote/$', views.vote, name='vote'),
]

