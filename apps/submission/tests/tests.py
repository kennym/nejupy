from django.test import TestCase, Client
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

import os

from submission.models import Submission
from submission.forms import SubmissionForm
from participant.models import Participant
from problem.models import Problem


SOURCE_CODE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               "sample_code")


class SubmissionTestCase(TestCase):
    """ Test the behaviour of submission. """
    fixtures = ["test_data.json"]
    
    def _get_source_file(self):
        source_file = os.path.join(SOURCE_CODE_DIR, "test.py")
        return source_file

    def get_source_code(self, pk=1):
        source_code = open(self._get_source_file(), 'rb')
        source_code = SimpleUploadedFile(source_code.name,
                                         source_code.read())
        return source_code

    def setUp(self):
        self.participant = Participant.objects.get(pk=1)
        self.problem = Problem.objects.get(pk=1)
        self.submission = Submission.objects.get(pk=1)
        self.client = Client()

    def test_create_submission(self):
        """ Test creating a submission. """
        source_code = File(open(os.path.join(SOURCE_CODE_DIR, "test.py")))
        submission = Submission(problem=self.problem,
                                participant=self.participant,
                                source_code=source_code,
                                programming_language=4)
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
                                source_code=source_code,
                                programming_language=4)
        submission.save()

        expected_path = os.path.abspath(
            "media/submissions/competition_{cid}/problem_{pid}/user_{uid}/test.py".
            format(
                cid=submission.participant.competition.id,
                pid=submission.problem.id,
                uid=submission.participant.id
            ))
        self.assertEquals(self.submission.source_code.path, expected_path)

    def test_submission_form(self):
        """ Test submission form. """
        problem = Problem.objects.get(pk=1)
        source_file = open(self._get_source_file(), 'rb')
        
        file_dict = {'source_code': 
                     SimpleUploadedFile(source_file.name, source_file.read())}
        form = SubmissionForm({"participant": self.participant.id,
                               "problem": problem.id,
                               "programming_language": 4},
                              file_dict)
        
        self.assertTrue(form.is_valid(), form.errors)

    def test_submit_to_problem(self):
        """ Test submitting submission. """
        # Log in as a participant
        self.client.login(username=self.participant.username, password="test")

        competition = self.participant.competition
        competition.start()
        self.assertTrue(competition.in_progress())

        problem = Problem.objects.get(pk=1)
        post_dict = {'source_code': self.get_source_code(),
                     'participant': self.participant.id,
                     'problem': problem.id,
                     "programming_language": 4}
        # Submit the problem
        response = self.client.post('/problem/%i/submit' % problem.id,
                                    post_dict, follow=True)

        # Should redirect to index
        self.assertEquals(response.status_code, 200)

    def test_submit_to_problem_while_competition_not_in_progress(self):
        """ Test submitting submission while competition is not in progress. """
        # Log in as a participant
        self.client.login(username=self.participant.username, password="test")

        # Make sure competition hasn't started, yet.
        competition = self.participant.competition
        competition.reset()
        self.assertFalse(competition.in_progress())

        problem = Problem.objects.get(pk=1)
        post_dict = {'source_code': self.get_source_code(pk=1),
                     'participant': self.participant.id,
                     'problem': problem.id,
                     'programming_language': 4}

        # Submit the problem
        response = self.client.post('/problem/%i/submit' % problem.id,
                                    post_dict, follow=True)
        
        self.assertEquals(response.status_code, 405)

    def test_submission_detail(self):
        """ Test submission_detail view. """
        self.client.login(username=self.participant.username, password="test")

        response = self.client.get('/submission/%i' % self.submission.id)

        self.assertEquals(response.status_code, 200)
