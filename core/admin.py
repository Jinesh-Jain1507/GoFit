from django.contrib import admin
from .models import Exercise, UserProfile

# Register your models here.

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exercise', 'weight', 'sets', 'reps', 'date']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
