from django.urls import path
from myapp.views.userviews import signup, login_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]
