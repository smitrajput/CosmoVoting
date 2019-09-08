from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from constituency.v1 import views

urlpatterns = [
    path('constituency/', views.ConstituencyList.as_view()),
    path('constituency/<int:pk>/', views.ConstituencyDetail.as_view()),
    path('constituency/<name>/candidate_list/', views.CandidateList.as_view()),
    path('constituency/<int:constituency_id>/add_candidate/', views.AddCandidate.as_view()),
    path('constituency/<int:constituency_id>/add_booth/', views.AddBooth.as_view()),
]
