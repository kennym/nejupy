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

from ideone import Ideone

from submission.forms import SubmissionForm
from submission.models import Submission
from problem.models import Problem

# Only participant decorator
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
        i = Ideone('kennym', 'supermind')
        result = i.create_submission(submission.source_code,
                                     language_id=submission.programming_language)
        details = i.submission_details(result['link'])
        submission.link = result["link"]
        submission.memory = details["memory"]
        submission.output = details["output"]
        submission.result = details["result"]
        submission.status = details["status"]
        submission.stderr = details["stderr"]
        submission.e_time = details["time"]
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
