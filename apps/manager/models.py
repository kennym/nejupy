from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from datetime import datetime, timedelta

COMPETITION_STATS = (
    (0, _('Not started')),
    (1, _('In Progress')),
    (2, _('Finished')),
)


class Competition(models.Model):
    """ The competition model. """
    
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'), max_length=1000)

    start_time = models.DateTimeField(_('Start time'), null=True, blank=True)
    end_time = models.DateTimeField(_('End time'), null=True, blank=True)
    
    status = models.SmallIntegerField(_('Status'),
                                      max_length=1,
                                      choices=COMPETITION_STATS,
                                      default=COMPETITION_STATS[0][0],
                                      null=False)
    
    def start(self):
        """ Start competition. """
        # Set status to 'In Progress'
        if self.status == COMPETITION_STATS[2][0]:
            return # Cannot start an already finished competition

        self.status = COMPETITION_STATS[1][0]
        self.start_time = datetime.now()
        
        self.save(force_update=True)

    def stop(self):
        """ Stop the competition. """
        if not self.start_time: 
            return # Cannot stop a competition that has not started
        if self.status == COMPETITION_STATS[2][0]:
            return # Cannot stop an already finished competition

        self.status = COMPETITION_STATS[2][0]
        self.end_time = datetime.now()

        self.save(force_update=True)

    def __unicode__(self):
        return self.title


class Team(models.Model):
    """ Team model. """
    name = models.CharField(_("Name"), max_length=55)


class Participant(User):
    """ The participant. """
    competition = models.ForeignKey(Competition)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.get_full_name()


class Problem(models.Model):
    """ The Problem model. """
    competition = models.ForeignKey(Competition)
    title = models.CharField(_("Title"), max_length=55)
    description = models.CharField(_("Description"), max_length=500)

    def __unicode__(self):
        return self.title

    
class Submission(models.Model):
    """ The Submission model. 

    A submission gets created by a participant, and refers to a
    problem. """
    participant = models.ForeignKey(Participant)
    problem = models.ForeignKey(Problem)
    source_code = models.FileField(_("Source Code"), upload_to="submissions")

    def __unicode__(self):
        return _("Submission: %s" % (self.id))
