
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('notes.urls')),
    path('account/',include('account.urls')),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

