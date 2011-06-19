from django.test import Client, TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from manager.models import Participant, Problem
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

    def test_submit_to_problem_form(self):
        problem = Problem.objects.get(pk=1)
        source_file = open(self._get_source_file(), 'rb')
        
        file_dict = {'source_code': SimpleUploadedFile(source_file.name, source_file.read())}
        form = SubmissionForm({"participant": self.p.id, "problem": problem.id}, file_dict)
        
        self.assertTrue(form.is_valid(), form.errors)

    def test_submit_to_problem(self):
        self.client.login(username=self.p.username, password="test")
        problem = Problem.objects.get(pk=1)
        source_file = self._get_source_file()

        post_dict = {'source_file': source_file,
                     'participant': self.p.id,
                     'problem': problem.id}
        #response = self.client.post(problem.submit_url(), post_dict)

        #self.assertEquals(response.status_code, 200)

