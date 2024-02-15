from django.urls import path
from . import views
from app import views as app_views

urlpatterns = [
    path('signout',app_views.signout,name="signout"),
    path('',views.index,name="lawyer"),
    path('lawyers',views.lawyers,name="lawyers"),
    path('profile',views.profile,name="profile"),
    path('happenings',views.happenings,name="happenings"),
    path('update_profile',views.update_profile,name="update_profile"),
]
