from django import forms 
from .models import Meal

class mealform(forms.modelform):
    class = Meta:
        model = Meal
        feilds = ['name', 'description', 'meal_type', 'calories', 'approved']
        