from django import template

register = template.Library()

@register.inclusion_tag('competition/templatetags/show_dashboard.html')
def show_dashboard(user):
    context = dict()
    context["user"] = user
    if hasattr(user, 'judge'):
        context["competition"] = user.judge.competition
    if hasattr(user, 'participant'):
        context["competition"] = user.participant.competition
    return context
