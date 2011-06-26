from django.test import TestCase, Client

from django.contrib.auth.models import User
from competition.models import Competition
from judge.models import Judge


class JudgeTestCase(TestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.competition = Competition.objects.get(pk=1)
        self.client = Client()
        self.judge = Judge.objects.all()[0]

    def test_create_judge(self):
        """ Test creating a judge. """
        judge = Judge(competition=self.competition,
                      username="test123",
                      password="test",
                      email="test@test.com")
        judge.save()

        self.assertIsNotNone(judge)

    def test_unicode_representation(self):
       """ Test the __unicode__() output. """
       participant = Judge(competition=self.competition,
                           first_name="First",
                           last_name="Last",
                           username="test",
                           password="test",
                           email="test@test.com")
       self.assertEquals(str(participant),
                         participant.get_full_name())

    def test_can_login(self):
        """ Test that judge can login. """
        self.client.login(username=self.judge, password="test")
