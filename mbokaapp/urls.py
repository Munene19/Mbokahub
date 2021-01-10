from django.urls import path
from mbokaapp import views

app_name = "mbokaapp"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('jobs/', views.job_list_View, name='job-list'),
    path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),

]
