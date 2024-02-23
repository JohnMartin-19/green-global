from django.urls import path
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('<int:pk>/', CategoryDetail.as_view(),name='category_detail'),
    path('', CategoryList.as_view(), name='category_list'),
]