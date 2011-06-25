from django.test import TestCase

from competition.models import Competition
from participant.models import Participant
from problem.models import Problem
from submission.models import Submission

from problem.templatetags.show_problems import get_problem_meta_for

class ProblemTestCase(TestCase):
    """ Tests for Problem model. """
    fixtures = ["test_data.json"]

    def setUp(self):
        self.problem = Problem.objects.get(pk=1)
        self.competition = Competition.objects.get(pk=1)

    def test_create_problem(self):
        """ Test creating a problem. """
        problem = Problem(competition=self.competition,
                          title="Test problem title",
                          description="Test problem description")
        problem.save()

        self.assertIsNotNone(Problem.objects.get(pk=problem.id))

    def test_unicode_representation(self):
        """ Test that unicode representation is correct. """
        self.assertEquals(str(self.problem), self.problem.title)

    def test_get_absolute_url(self):
        url = self.problem.get_absolute_url()

        self.assertEquals(url, u'/problem/%i' % self.problem.id)

    def test_get_submit_url(self):
        url = self.problem.submit_url()

        self.assertEquals(url, u'/problem/%i/submit' % self.problem.id)


class TemplateTagTestCase(TestCase):
    """ Tests for template tags. """
    fixtures = ["test_data.json"]

    def setUp(self):
        self.participant = Participant.objects.get(pk=1)

    def test_get_problem_meta(self):
        """ Test get_problem_meta_for helper function. """
        problem_meta = get_problem_meta_for(self.participant)

        problem = Problem.objects.get(pk=1)
        submission = Submission.objects.get(problem=problem)

        self.assertEquals(problem_meta,
                          [{"submissions": 1,
                            "problem": problem,
                            "submission": submission}])
