from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import (
    render_to_response,
    RequestContext
)

@login_required
def judge_dashboard(request, template_name="judge/dashboard.html"):
    user = request.user
    if hasattr(user, 'judge'):
        problems = user.judge.competition.problem_set.all()
        participants = user.judge.competition.participant_set.all()

        context = {
            "problems": problems,
            "participants": participants
        }
    
        return render_to_response(template_name,
                                  context,
                                  context_instance = RequestContext(request))
