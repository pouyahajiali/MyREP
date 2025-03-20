import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.models import UserProfile, WorkoutProgress 
from .models import WorkoutPlan
from django.contrib import messages


@login_required
def workout_dashboard(request):
    # Get the current user's profile
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    # Start with all workout plans
    plans = WorkoutPlan.objects.all()
    

    if profile and profile.fitness_goals:
        plans = plans.filter(goal=profile.fitness_goals.lower())

    # get the user's current plan
    if request.user.userprofile.workout_plan:
        curr_plan = request.user.userprofile.workout_plan
        context = {
            'curr_plan' : curr_plan,
            'profile': profile,
            'plans': plans,
        }
    else:
        context = {
            'profile': profile,
            'plans': plans,
        }
    
    return render(request, 'workout_plans.html', context)


@login_required
def workout_plan_view(request):
    if request.method == "POST":
        selected_plan_id = request.POST.get("selected_plan")
        if selected_plan_id:
            try:
                selected_plan = WorkoutPlan.objects.get(id=selected_plan_id)
                request.user.userprofile.workout_plan = selected_plan
                request.user.userprofile.save()
                messages.success(request, f"You have successfully chosen the {selected_plan.name} plan!")
                return redirect("dashboard")
            except WorkoutPlan.DoesNotExist:
                messages.error(request, "Invalid Workout Plan Selected.")
        else:
            messages.error(request, "Please select a workout plan.")
    return redirect("workout_dashboard")

@login_required
def my_plan_view(request):
    curr_plan = request.user.userprofile.workout_plan
    context = {
        "weekly_plan" : curr_plan.weekly_plan
    }
    return render(request, "myplan.html", context)


@login_required
def calc_calories(request):
    if request.method == "POST":
        duration_minutes = request.POST.get("duration_minutes")
        calories_burned = request.POST.get("calories_burned")
        try:
            duration_minutes = int(duration_minutes)
            calories_burned = int(calories_burned)
        except (TypeError, ValueError):
            return JsonResponse({"error": "Invalid numeric values."}, status=400)
        
        progress = WorkoutProgress.objects.create(
            user=request.user,
            workout_type=request.user.userprofile.fitness_goals.lower(),
            duration_minutes=duration_minutes,
            calories_burned=calories_burned,
        )
        return JsonResponse({"status": "success", "progress_id": progress.id})
    
    return JsonResponse({"error": "POST request required."}, status=405)
        