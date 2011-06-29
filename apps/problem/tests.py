from django.test import TestCase, Client

from competition.models import Competition
from participant.models import Participant
from problem.models import Problem
from submission.models import Submission

from problem.templatetags.show_problems import get_problem_meta_for, _get_problem_dict_for


class ViewsTestCase(TestCase):
    """ Test views of application. """
    fixtures = ["test_data.json"]

    def setUp(self):
        self.client = Client()
        self.participant = Participant.objects.get(pk=1)

    def test_problem_detail(self):
        """ Test getting problem detail. """
        self.client.login(username=self.participant.username,
                          password="test")

        problem = Problem.objects.all()[0]
        response = self.client.get('/problem/%i' % problem.id)
        self.assertEquals(response.status_code, 200)


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

class TemplateTagTestCase(TestCase):
    """ Tests for template tags. """
    fixtures = ["test_data.json"]

    def setUp(self):
        self.participant = Participant.objects.get(pk=1)

    def test_get_problem_dict_for(self):
        """ Test _get_problem_dict_for() method. """
        problems = self.participant.competition.problem_set.all()
        for problem in problems:
            problem_dict = _get_problem_dict_for(problem)
            self.assertEquals(len(problem_dict["submission"]),
                              len(problem.submission_set.filter(participant=self.participant,
                                                                           problem=problem)))
            self.assertEquals(problem_dict["problem"],
                              problem) 

    def test_get_problem_meta(self):
        """ Test get_problem_meta_for helper function. """
        problem_meta = get_problem_meta_for(self.participant)

        meta = []
        for problem in self.participant.competition.problem_set.all():
            new_dict = _get_problem_dict_for(problem)
            meta.append(new_dict)

        self.assertEquals(len(problem_meta),
                          len(meta))
