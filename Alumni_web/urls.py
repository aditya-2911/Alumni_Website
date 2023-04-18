from django.urls import path, include

from .views import home_page, login_page

urlpatterns = [
    path('',home_page),
    path('login/',login_page,name='login'),
    # path('accounts/', include('allauth.urls')),
]