from django.urls import path, include
from .import views
app_name = 'project'
urlpatterns = [
    path('', views.proDetail, name='project'),
    path('<int:id>/', views.proDetail, name = 'proDetail'),
]
