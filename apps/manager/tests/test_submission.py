from django.test import TestCase
from django.core.files import File

import os

from manager.models import (
    Submission,
    Participant,
    Problem
)

SOURCE_CODE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               "sample_code")


class SubmissionTestCase(TestCase):
    """ Test the behaviour of submission. """
    fixtures = ["test_data.json"]
    
    def setUp(self):
        self.participant = Participant.objects.get(pk=1)
        self.problem = Problem.objects.get(pk=1)
        self.submission = Submission.objects.get(pk=1)

    def test_create_submission(self):
        """ Test creating a submission. """
        source_code = File(open(os.path.join(SOURCE_CODE_DIR, "test.py")))
        submission = Submission(problem=self.problem,
                                participant=self.participant,
                                source_code=source_code)
        submission.save()

        self.assertIsNotNone(Submission.objects.get(pk=submission.id))
    
    def test_unicode_representation(self):
        """ Test that unicode representation is correct. """
        self.assertEquals(str(self.submission),
                          "Submission: %s" % self.submission.id)

    def test_source_code_upload_path(self):
        """ Test that source code gets saved in correct path. """
        source_code = File(open(os.path.join(SOURCE_CODE_DIR, "test.py")))
        submission = Submission(problem=self.problem,
                                participant=self.participant,
                                source_code=source_code)
        submission.save()

        expected_path = os.path.abspath(
            "media/submissions/competition_{cid}/problem_{pid}/user_{uid}/test.py".
            format(
                cid=submission.participant.competition.id,
                pid=submission.problem.id,
                uid=submission.participant.id
            ))
        self.assertEquals(self.submission.source_code.path, expected_path)
