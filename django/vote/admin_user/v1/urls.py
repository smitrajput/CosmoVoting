from django.conf.urls import url

from admin_user.v1 import views

urlpatterns = [
    url(r'^admin/register/', views.AdminUserRegistration.as_view(),
        name='v1_AdminUserRegistration'),
    url(r'^admin/login/', views.AdminUserLogin.as_view(), name='v1_AdminUserLogin'),
    url(r'^admin/logout/$', views.AdminUserLogout.as_view(),
        name='v1_AdminUserLogout'),
    url(r'^admin/config/$', views.Config.as_view(), name='v1_config'),
]
