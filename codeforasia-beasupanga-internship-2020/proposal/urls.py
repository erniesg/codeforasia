from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='proposal_index'),
    path('login/', views.loginPage, name='proposal_login'),
    path('register/', views.registerPage, name='proposal_register'),
    path('logout/', views.logoutPage, name='proposal_logout'),
]
