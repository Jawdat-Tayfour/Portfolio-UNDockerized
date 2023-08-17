from django.urls import path

from .views import  AboutView,game_dev_project_list,web_dev_project_list,ProjectDetailView

urlpatterns = [
    path('',AboutView.as_view(),name='about'),
    path('game_dev_project_list/',game_dev_project_list,name='game_dev_project_list'),
    path('web_dev_project_list/',web_dev_project_list,name='web_dev_project_list'),
    path('<uuid:pk>',ProjectDetailView.as_view(),name='project_detail'),
    ]