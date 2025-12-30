from django import forms

from .models import SubscriptionPlans

class SubscriptionPlanForm(forms.ModelForm):

    class Meta:

        model = SubscriptionPlans

        fields = "__all__"

        exclude = ['uuid', 'active_status']



