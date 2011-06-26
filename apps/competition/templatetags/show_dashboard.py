from django import template

register = template.Library()

@register.inclusion_tag('competition/templatetags/show_dashboard.html')
def show_dashboard(user):
    context = dict()
    if user.participant:
        competition = user.participant.competition
        
        context["competition"] = competition
        context["participant"] = user.participant

        return context
