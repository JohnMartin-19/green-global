
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include ('rest_framework.urls')), # for token authentication
    path('api/v1/users/',include('users.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/orders/',include('orders.urls')),
    path('api/v1/categories/' ,include('categories.urls')),
    path('api/v1/reviews/', include(('reviews.urls'))),
    #url path for auth
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
]

admin.site.site_header = "Green-Global Admin"
admin.site.site_title = "Green-Global Admin Portal"
admin.site.index_title = "Welcome to Green-Global Portal"