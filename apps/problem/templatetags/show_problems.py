from django import template
from submission.models import Submission

register = template.Library()

@register.inclusion_tag('problem/templatetags/show_problems.html')
def show_problems(participant):
    """ Return all problems for the `participant` """
    problems = participant.competition.problem_set.all()

    problem_meta = []
    for problem in problems:
        new_dict = {"solved": False,
                    "submissions": 0,
                    "problem": None,
                    "submission": None}
        for submission in problem.submission_set.filter(participant=participant):
            # Add a submission
            new_dict["submissions"] += 1
            #if submission.result_correct():
            #    new_dict["solved"] = True
            #    # Add problem to dict
            new_dict["submission"] = submission
        new_dict["problem"] = problem
        problem_meta.append(new_dict)

    context = {
        "problems": problem_meta,
        "participant": participant
    }

    return context

