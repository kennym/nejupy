from django.test import TestCase, Client

from django.contrib.auth.models import User
from competition.models import Competition
from participant.models import Team, Participant



class TeamTestCase(TestCase):

    def test_create_team(self):
        """ Test creating a team. """
        team = Team.objects.create(name="Test team")
        team.save()


class ParticipantTestCase(TestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.competition = Competition.objects.get(pk=1)
        self.team = Team.objects.get(pk=1)
        self.client = Client()
        self.participant = Participant.objects.get(pk=1)

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

#    def test_visit_index_as_participant(self):
#        """ Test visiting index as a participant. """
#        # Login as a user
#        self.client.login(username=self.participant.username, password="test")
#        # Visit the index
#        response = self.client.get('/')
# 
#        self.assertEquals(response.status_code, 200)

