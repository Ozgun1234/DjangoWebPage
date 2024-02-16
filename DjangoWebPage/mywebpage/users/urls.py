
from django.urls import path
from .views import home, RegisterView, profile, job_seeker, details, employer  # Import the view here

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('members/', job_seeker, name='members'),
    path('employer/', employer, name='members'),
    path('members/details/<str:username>', details, name='details'),
    path('employer/details/<str:username>', details, name='details'),
]