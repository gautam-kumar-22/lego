from django.urls import path

from . import views

urlpatterns = [
    path('sign-up/', views.SignUpApiView.as_view(), name='sign-up'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view(), name='logout'),
]
