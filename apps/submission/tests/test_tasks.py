from submission.tasks import get_ideone_result_for
from submission.models import Submission

from django.test import TestCase, Client


class TasksTestCase(TestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.submission = Submission.objects.all()[0]

    def test_get_ideone_result(self):
        """ Test getting Ideone result. """
        result = get_ideone_result_for.delay(submission_id=self.submission.id)

        self.assertEquals(result.successful(), True)

