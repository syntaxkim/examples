from django.urls import path
from . import views

app_name = 'polls'

""" Function-based views """
urlpatterns = [
    path('', views.index, name='index'), # /polls/
    path('<int:question_id>/', views.detail, name='detail'), # /polls/<int>
    path('<int:question_id>/results/', views.results, name='results'), # /polls/<int>/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # /polls/<int>/vote/
]

""" Class-based views """
urlpatterns2 = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]