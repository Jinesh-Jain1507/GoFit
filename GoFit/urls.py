from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('workouts/<str:date>', views.workouts, name="workouts"),
    path('workouts', views.workout_redirect, name="workout"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('yoga', views.yoga, name="yoga"),
    path('yoga/<int:id>', views.yogaasana, name="yogaasana"),
    path('calories', views.calories, name="calories"),
    path('chat', views.chat, name="chat"),
    path('faq', views.faq, name="faq"),
    path('contact', views.contact, name="contact"),
    path('profile/<int:id>', views.profile, name="profile"),
    path('delete/<int:id>', views.delete, name="delete"),
]

