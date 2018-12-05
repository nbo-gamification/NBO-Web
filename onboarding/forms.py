from django import forms

from onboarding.models import (
    Briteling,
    CategoryOfficeActivity,
    ConnectActivity,
    Office,
)

class ConnectForm(forms.Form):

    instructions = forms.CharField(widget=forms.Textarea)

    solution_code = forms.CharField(max_length=60)

    class Meta:
        model = ConnectActivity

class BritelingForm(forms.Form):

    name = office_name = forms.CharField(
        max_length=60,
    )

    briteling_image = forms.ImageField(
    )

    class Meta:
        model = Briteling
        fields = ['name', 'briteling_image']
        exclude = ['position']

class CategoryOfficeActivityForm(forms.Form):
    points_reward = forms.IntegerField()

    class Meta:
        model = CategoryOfficeActivity
        field = ['points_reward']

class OfficeForm(forms.Form):

    office = forms.ModelChoiceField(
        queryset=Office.objects.all().order_by('id'),
    )
