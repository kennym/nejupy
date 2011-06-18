from django.test import TestCase

from manager.models import Team


class TeamTestCase(TestCase):

    def test_create_team(self):
        """ Test creating a team. """
        team = Team.objects.create(name="Test team")
        team.save()
