from django.db import models

class Meal(models.Model):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'

    MEAL_TYPE_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    meal_type = models.CharField(
        max_length=50,
        choices=MEAL_TYPE_CHOICES
    )
    calories = models.PositiveIntegerField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    