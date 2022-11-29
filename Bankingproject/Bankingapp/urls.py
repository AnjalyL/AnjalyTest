
from django.urls import path
from  . import views
app_name = 'Bankingapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/register/',views.register,name='register'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('login/form/',views.form,name='form'),
    path('form/',views.form,name='form'),
    path('logout',views.logout,name='logout'),



]
