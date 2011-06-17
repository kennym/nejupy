from django.utils import unittest

from django.contrib.auth.models import User
from manager.models import (
    Competition,
    Team,
    Profile,
)


class ParticipantTestCase(unittest.TestCase):

    def test_create_participant(self):
        """ Test creating a participant. """
        participant = User.objects.create_user(username="test",
                                               email="test@test.com")
        participant.save()

        self.assertIsNotNone(participant)

    def test_is_participant(self):
        """ Test that user is a participant. """
        participant = User(username="test2",
                           email="test@test.com",
                           password="test")
        participant.save()

        competition = Competition.objects.create(title="Test", description="test")
        team = Team.objects.create(name="Test")
        competition.save()
        team.save()

        profile = Profile(user=participant,
                          is_participant=True,
                          competition=competition,
                          team=team)
        profile.save()

        self.assertIsNotNone(participant)
        self.assertTrue(participant.get_profile().is_participant)
        
