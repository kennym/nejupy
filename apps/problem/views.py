from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import (
    redirect,
    get_object_or_404,
    render_to_response,
    RequestContext
)

from problem.models import Problem
from submission.forms import SubmissionForm


@login_required
def problem_detail(request, id, template_name="problem/detail.html"):
    problem = get_object_or_404(Problem, pk=id)

    return render_to_response(template_name,
                              {'problem': problem,
                               'form': SubmissionForm},
                              context_instance=RequestContext(request))
                              
                              

