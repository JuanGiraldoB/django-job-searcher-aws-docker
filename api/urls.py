from django.urls import path
from . import views


urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name='job-list'),
    path('', views.CategoryListView.as_view(), name='category-list'),
    path('jobs/<str:category_id>/',
         views.JobsByCategoryView.as_view(), name='jobs-by-category'),
]
