from django.urls import path
from .views import create_issue, list_issues

urlpatterns = [
    path('create/', create_issue, name='create_issue'),
    path('', list_issues, name='list_issues'),
]