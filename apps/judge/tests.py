from django.test import TestCase, Client

from django.contrib.auth.models import User
from competition.models import Competition
from judge.models import Judge


class JudgeTestCase(TestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.competition = Competition.objects.get(pk=1)
        self.judge = Judge.objects.all()[0]

    def test_create_judge(self):
        """ Test creating a judge. """
        judge = Judge(competition=self.competition,
                      username="test_j",
                      password="test",
                      email="test@test.com")
        judge.save()

        self.assertIsNotNone(judge)

    def test_judge_can_login(self):
        # Login as a user
        self.client.login(username=self.judge.username, password="test")
        # Visit the index
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

    def test_redirect_to_dashboard_after_login(self):
        self.client.login(username=self.judge.username, password="test")

        response = self.client.get('/')

        self.assertRedirects(response, '/judge/dashboard')
