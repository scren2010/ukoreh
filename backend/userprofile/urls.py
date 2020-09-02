from django.urls import path

from backend.userprofile import views



urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user-update/', views.UpdateUserView.as_view()),


    path('profile/', views.ProfileView.as_view()),

    path('accounts/google/login/', views.social_login)

]
