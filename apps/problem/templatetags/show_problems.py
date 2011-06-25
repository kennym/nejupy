from django import template
from submission.models import Submission


def get_problem_meta_for(participant):
    """ Return all problems with a submission from the `participant`.

    @return dict
    """
    problems = participant.competition.problem_set.all()

    problem_meta = []
    for problem in problems:
        new_dict = {"submissions": 0,
                    "problem": None,
                    "submission": None}
        for submission in problem.submission_set.filter(participant=participant):
            # Add a submission
            new_dict["submissions"] += 1
            new_dict["submission"] = submission
        new_dict["problem"] = problem
        problem_meta.append(new_dict)
    
    return problem_meta
       

register = template.Library()

@register.inclusion_tag('problem/templatetags/show_problems.html')
def show_problems(participant):
    """ Return all problems for the `participant` """

    context = {
        "problems": get_problem_meta_for(participant),
        "participant": participant
    }

    return context
