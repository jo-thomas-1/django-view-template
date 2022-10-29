from django.urls import path
from . import views # importing views module from current folder

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('detail', views.detail, name='detail'),
    path('thanks', views.thanks, name='thanks')
]
