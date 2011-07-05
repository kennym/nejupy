from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, HttpResponse
from django.views.decorators.http import require_POST
from django.utils import simplejson
from django.shortcuts import (
    redirect,
    get_object_or_404,
    render_to_response,
    RequestContext
)

from submission import tasks
from submission.forms import SubmissionForm
from submission.models import Submission
from problem.models import Problem

@login_required
@require_POST
def submit_for_problem(request, id):
    user = request.user
    if not user.participant.competition.in_progress():
        return HttpResponseNotAllowed("Competition not in progress.")

    form = SubmissionForm(request.POST, request.FILES)
    if form.is_valid():
        submission = form.save(commit=False)
        submission.competition = user.participant.competition
        submission.participant = user.participant
        submission.problem = get_object_or_404(Problem, pk=id)
        submission.save()

        return redirect('/',
                        context_instance=RequestContext(request))
    else:
        return redirect('/',
                        {"form": form},
                        context_instance=RequestContext(request))

@login_required
def submission_detail(request, id, template_name="submission/detail.html"):
    submission = get_object_or_404(Submission, pk=id)
    
    return render_to_response(template_name,
                              {"submission": submission},
                              context_instance=RequestContext(request))
