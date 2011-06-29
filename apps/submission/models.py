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

LANGUAGES = (
 (1, "C++ (gcc-4.3.4)"),
 (2, "Pascal (gpc) (gpc 20070904)"),
 (3, "Perl (perl 5.12.1)"),
 (4, "Python (python 2.6.4)"),
 (10, "Java (sun-jdk-1.6.0.17)"),
 (11, "C (gcc-4.3.4)"),
 (17, "Ruby (ruby-1.9.2)"),
 (22, "Pascal (fpc) (fpc 2.2.0)"),
 (29, "PHP (php 5.2.11)"),
 (35, "JavaScript (rhino) (rhino-1.6.5)"),
 (40, "SQL (sqlite3-3.7.3)"),
 (44, "C++ (gcc-4.5.1)"),
 (45, "Assembler (gcc-4.3.4)"),
 (101, "Visual Basic .NET (mono-2.4.2.3)"),
 (114, "Go (gc-2010-07-14)"),
 (116, "Python 3 (python-3.1.2)")
)

class Submission(models.Model):
    """ The Submission model. 

    A submission gets created by a participant, and refers to a
    problem. """
    participant = models.ForeignKey(Participant)
    problem = models.ForeignKey(Problem)
    source_code = models.FileField(_("Source Code"), upload_to=get_upload_path)
    programming_language = models.SmallIntegerField(_("Programming language"),
                                                    choices=LANGUAGES)

    link = models.CharField(_("Link"), max_length=5, blank=True, null=True)
    memory = models.IntegerField(_("Memory usage"), blank=True, null=True)
    output = models.CharField(_("Output"), max_length=10,
                              blank=True, null=True,)
    result = models.IntegerField(_("Result"), blank=True, null=True)
    status = models.IntegerField(_("Status"), blank=True, null=True)
    stderr = models.TextField(_("Error Output"), blank=True, null=True)
    e_time = models.FloatField(_("Execution time"),
                                 blank=True, null=True)

    def __unicode__(self):
        return _("Submission: %s" % (self.id))
