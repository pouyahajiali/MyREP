from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.workout_dashboard, name='workout_dashboard'),
    path("workout-plan/", views.workout_plan_view, name="workout_plan"),
    path("myplan/", views.my_plan_view, name="my_plan"),
    path("calccalories/", views.calc_calories, name="calc_calories"),

]
