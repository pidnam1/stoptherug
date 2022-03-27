from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('searched/', views.searched, name='searched'),
    path('about/', views.about, name='about'),
    path('report/<int:nft_id>/', views.report, name='report'),
    path('vote/<int:nft_id>/', views.vote, name='vote'),
    path(r'captcha/', include('captcha.urls'))
]