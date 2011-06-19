from django import forms
from manager.models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
