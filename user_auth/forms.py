# forms.py

from django import forms
from admin_auth.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_user', 'review_comment']
