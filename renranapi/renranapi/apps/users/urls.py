from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path

urlpatterns = [
    path(r'authorizations/', obtain_jwt_token, name='authorizations'),
]
