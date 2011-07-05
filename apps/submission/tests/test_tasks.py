from submission import tasks
from submission.models import Submission

from django.conf import settings
from django.test import TestCase, Client


class TasksTestCase(TestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.submission = Submission.objects.all()[0]
        settings.CELERY_ALWAYS_EAGER = True
        self.ideone_link = "tiFZT"

    def test_create_ideone_submission(self):
        """ Test creating Ideone submission. """
        result = tasks.create_ideone_submission.delay(self.submission.source_code.read(),
                                                      self.submission.programming_language)

        self.assertEquals(result.successful(), True)
        self.assertEquals(isinstance(result.result, dict), True)

    def test_get_submission_details(self):
        """ Test `get_submission_details` task. """
        result = tasks.get_submission_details.delay(self.ideone_link)

        self.assertEquals(result.successful(), True)
        self.assertEquals(isinstance(result.result, dict), True)
        self.assertEquals(result.result["link"], self.ideone_link)


