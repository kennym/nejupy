from django.test import TestCase

from django.contrib.auth.models import User
from manager.models import (
    Competition,
    Team,
    Participant,
)


class ParticipantTestCase(TestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.competition = Competition.objects.get(pk=1)
        self.team = Team.objects.get(pk=1)

    def test_create_participant(self):
        """ Test creating a participant. """
        participant = Participant(competition=self.competition,
                                  team=self.team,
                                  username="test",
                                  password="test",
                                  email="test@test.com")
        participant.save()

        self.assertIsNotNone(participant)

    def test_unicode_representation(self):
       """ Test the participant model __unicode__() output. """
       participant = Participant(competition=self.competition,
                                 team=self.team,
                                 first_name="First",
                                 last_name="Last",
                                 username="test",
                                 password="test",
                                 email="test@test.com")
       self.assertEquals(str(participant),
                         participant.get_full_name())
