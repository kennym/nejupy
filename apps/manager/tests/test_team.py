from django.utils import unittest

from manager.models import Team


class TeamTestCase(unittest.TestCase):

    def test_create_team(self):
        """ Test creating a team. """
        team = Team.objects.create(name="Test team")
        team.save()
