from django import forms
from submission.models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('source_code', 'programming_language')
