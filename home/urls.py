from django.urls import path, include
from .import views
app_name = 'home'
urlpatterns = [
    path('', views.Index2.as_view(), name='home'),
    path('<int:id>/', views.cateDetail, name='cateDetail'), # lan sau nen viet nhu the nhe
    # khong nen viet name = . hay viet name=value
    # khi khai bao bien thi moi : name = 5
]
