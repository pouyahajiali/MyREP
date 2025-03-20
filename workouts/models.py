from django.db import models

class WorkoutPlan(models.Model):
    # workout goals
    GOAL_CHOICES = [
        ("weight_loss", "Weight Loss & Fat Burn"),
        ("muscle_gain", "Muscle Gain & Strength Training"),
        ("endurance", "Endurance & Stamina Boost"),
        ("flexibility", "Flexibility & Mobility"),
        ("core_strength", "Core & Functional Strength"),
        ("balanced_fitness", "Balanced Fitness & Well-being"),
        ("athletic_performance", "Athletic Performance & Conditioning"),
        ("custom_wellness", "Customized & Holistic Wellness"),
    ]
    #intensity.
    INTENSITY_CHOICES = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
    ]
    
    name = models.CharField(max_length=150)
    description = models.TextField()
    goal = models.CharField(max_length=50, choices=GOAL_CHOICES, default='balanced_fitness')
    duration_minutes = models.IntegerField(help_text="Total workout duration in minutes")
    intensity = models.CharField(max_length=20, choices=INTENSITY_CHOICES, default='moderate')
    created_at = models.DateTimeField(auto_now_add=True)
    weekly_plan = models.JSONField(default=dict, blank=True, null=True, help_text="Full week daily workout plan as JSON")


    def __str__(self):
        return self.name
