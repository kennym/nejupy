from django.db import models
from django.utils.translation import ugettext as _

import os

from participant.models import Participant
from problem.models import Problem


def get_upload_path(instance, filename):
    """ Return custom upload path for Submission. """
    return os.path.join(
        "submissions/competition_{cid}/problem_{pid}/user_{uid}/{filename}".format(
        cid=instance.participant.competition.id,
        pid=instance.problem.id,
        uid=instance.participant.id,
        filename=filename))


class Submission(models.Model):
    """ The Submission model. 

    A submission gets created by a participant, and refers to a
    problem. """
    participant = models.ForeignKey(Participant)
    problem = models.ForeignKey(Problem)
    source_code = models.FileField(_("Source Code"), upload_to=get_upload_path)

    def __unicode__(self):
        return _("Submission: %s" % (self.id))
