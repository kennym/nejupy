from django import template
from submission.models import Submission
from submission.forms import SubmissionForm


def _get_problem_dict_for(problem):
    new_dict = dict()
    new_dict["submission"] = Submission.objects.filter(problem=problem)
    new_dict["problem"] = problem

    return new_dict

def get_problem_meta_for(participant):
    """ Return all problems with a submission from the `participant`.

    @return dict
    """
    problems = participant.competition.problem_set.all()

    problem_meta = []
    for problem in problems:
        problem_meta.append(_get_problem_dict_for(problem))
    
    return problem_meta
       

register = template.Library()

@register.inclusion_tag('problem/templatetags/show_problems.html')
def show_problems(participant):
    """ Return all problems for the `participant` """

    context = {
        "problems": get_problem_meta_for(participant),
        "participant": participant,
        "form": SubmissionForm
    }

    return context
