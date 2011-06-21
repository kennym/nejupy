from django.test import Client, TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from manager.models import (
    Participant,
    #Judge,
    Problem,
    Submission
)

from manager.forms import SubmissionForm

import os


SOURCE_CODE_DIR = os.path.abspath(os.path.dirname(__file__))


class ApplicationTestCase(TestCase):
    """ Test the apps' front-end behavior. """
    fixtures = ["test_data.json"]
    
    def _get_source_file(self):
        source_file = os.path.join(SOURCE_CODE_DIR, "sample_code/test.py")
        return source_file

    def setUp(self):
        self.client = Client()
        self.p = Participant.objects.get(pk=1)
        self.judge = None

    def test_visit_index_as_visitor(self):
        """ Test visiting index as a visitor.

        Visitor should be redirected to login page.
        """
        response = self.client.get('/')

        self.assertEquals(response.status_code, 302)
    
    ####################################################################
    # Participant tests
    ####################################################################
    def test_visit_index_as_participant(self):
        """ Test visiting index as a participant. """
        # Login as a user
        self.client.login(username=self.p.username, password="test")
        # Visit the index
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

    def test_submission_form(self):
        """ Test submission form. """
        problem = Problem.objects.get(pk=1)
        source_file = open(self._get_source_file(), 'rb')
        
        file_dict = {'source_code': 
                     SimpleUploadedFile(source_file.name, source_file.read())}
        form = SubmissionForm({"participant": self.p.id,
                               "problem": problem.id},
                              file_dict)
        
        self.assertTrue(form.is_valid(), form.errors)

    def test_submit_to_problem(self):
        """ Test submitting submission. """
        # Log in as a participant
        self.client.login(username=self.p.username, password="test")

        problem = Problem.objects.get(pk=1)
        source_code = open(self._get_source_file(), 'rb')
        post_dict = {'source_code': SimpleUploadedFile(source_code.name,
                                                       source_code.read()),
                     'participant': self.p.id,
                     'problem': problem.id}
        response = self.client.post(problem.submit_url(), post_dict, follow=True)

        # Should redirect to index
        self.assertEquals(response.redirect_chain[0][0], "http://testserver/")
        self.assertEquals(response.status_code, 200)

    ####################################################################
    # Judge tests
    ####################################################################
#    def test_submit_to_problem_as_judge(self):
#        """ Test submitting submission as a judge. """
#        # Log in as a participant
#        self.client.login(username=self.p.username, password="test")
#
#        problem = Problem.objects.get(pk=1)
#        source_code = open(self._get_source_file(), 'rb')
#       post_dict = {'source_code': SimpleUploadedFile(source_code.name,
#                                                      source_code.read()),
#                    'participant': self.p.id,
#                    'problem': problem.id}
#       response = self.client.post(problem.submit_url(), post_dict, follow=True)
