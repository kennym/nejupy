from django.db import models
from django.utils.translation import ugettext as _

from competition.models import Competition


class Problem(models.Model):
    """ The Problem model. """
    competition = models.ForeignKey(Competition)
    title = models.CharField(_("Title"), max_length=55)
    description = models.CharField(_("Description"), max_length=500)
    
    @models.permalink
    def get_absolute_url(self):
        return ('problem.views.problem_detail', [str(self.id)])

    @models.permalink
    def submit_url(self):
        return ('problem.views.submit_to_problem', [str(self.id)])

    def __unicode__(self):
        return self.title


