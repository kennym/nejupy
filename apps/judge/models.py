from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from competition.models import Competition


class Judge(User):
    competition = models.ForeignKey(Competition)

    def __unicode__(self):
        return self.get_full_name()
