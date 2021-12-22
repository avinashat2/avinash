from django.urls import path,include
from. import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('log-in/', views.Loginhandle, name='login'),
    path('log-out/', views.Logouthandle, name='logout'),
    path('contact-us/', views.ContactUs, name='contactus'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('reply/<int:id>/', views.Replyhandle, name='reply'),
    
]
