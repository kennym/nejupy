from django.utils import unittest

from manager.models import (
    Competition,
    Team,
    Participant,
)


class ParticipantTestCase(unittest.TestCase):

    def test_create_participant(self):
        """ Test creating a participant. """
        competition = Competition.objects.create(title="Test", description="test")
        team = Team.objects.create(name="Team")
        participant = Participant.objects.create(competition=competition,
                                                 team=team)
        participant.save()

    #def test_can_authenticate(self):
