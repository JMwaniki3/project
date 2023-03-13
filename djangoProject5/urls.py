from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('convo/',views._messages, name='_messages'),
    path('navbar/',views._navbar, name='_navbar'),
    path('home/',views.base, name='base'),
    path('passchange/',views.change_password, name='change_password'),
    path('details/',views.detail, name='details'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('results/',views.results, name='results')
]
