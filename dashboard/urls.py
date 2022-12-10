from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('/<str:page>/', views.home), 
    path('dashboard/<int:res_id>', views.dashboard, name='dashboard'),
    path('compare/<int:res_id1>-<int:res_id2>', views.compare_2_vendors, name='compare') # compare/<int:res_id1>-<int:res_id2>
]
