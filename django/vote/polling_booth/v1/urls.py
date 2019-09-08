from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from polling_booth.v1 import views

urlpatterns = [
    path('polling_booth/', views.PollingBoothList.as_view()),
    path('polling_booth/<int:pk>/', views.PollingBoothDetail.as_view()),
]
