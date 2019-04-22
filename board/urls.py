from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('races/', views.races_list, name='races'),
    path('accounts/register', views.register, name='register'),
    path('races/<uuid:id>', views.race_detail, name='race-detail')
]
