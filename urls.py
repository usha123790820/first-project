from django.contrib import admin
from django.urls import path
from codeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('user/', views.user_page, name='user_page'),
    path('logout/', views.logout_view, name='logout'),
]