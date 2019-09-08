from django.conf.urls import url

from election.v1 import views

urlpatterns = [
    url(r'^election/update_status/', views.UpdateStatus.as_view(),
        name='v1_update_status'),
    url(r'^elections/', views.ElectionList.as_view(),
        name='v1_election'),
    
]
