from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from competition.models import Competition


class Team(models.Model):
    """ Team model. """
    name = models.CharField(_("Name"), max_length=55)


class Participant(User):
    """ The participant. """
    competition = models.ForeignKey(Competition)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.get_full_name()


