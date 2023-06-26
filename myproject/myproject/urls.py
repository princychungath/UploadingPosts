from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # other URL patterns
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
    # other URL patterns
]
