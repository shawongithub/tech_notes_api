from django.urls import path
from account import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

app_name='account'

urlpatterns = [
    path('signup/', views.signup, name='sign-up'),
    path('login/', obtain_auth_token, name='login'),  # <-- And here
]
