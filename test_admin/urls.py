from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='admin_test_list'),
    # path('test/<int:id>/', views.test_view, name='test_view')
    path('add/', views.test_add, name='admin_test_add'),
    path('results/', views.test_results_view, name='results'),
    # Thêm các URL khác nếu cần
]
