from django.urls import path
from static import views

urlpatterns = [
    path('basic/', views.StaticBasic.as_view()),
    path('basic/detail/<int:primary_key>/', views.StaticBasicDetail.as_view())
]
