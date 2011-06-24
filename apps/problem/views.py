from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect,
)

from submission.forms import SubmissionForm


@login_required
def submit_to_problem(request, id):
    user = request.user
    if request.method == "POST":
        if user.participant:
            form = SubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            return 

@login_required
def problem_detail(request, id):
    pass

