from django.urls import path
from .views import UserList, UserDetail,RegisterView,protected_route
urlpatterns = [
path("<int:pk>/", UserDetail.as_view(), name="user_detail"),
path("", UserList.as_view(), name="user_list"),
path('register/', RegisterView.as_view(), name='Register'),
path('protected_route/',protected_route, name='Protected_route')
]