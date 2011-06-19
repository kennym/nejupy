from lettuce import *
from django.test.client import Client
from lettuce.django import django_url

from manager.models import Participant, Submission

@before.all
def set_browser():
    world.browser = Client()

@step(r'Given A Participant with username "(.*)"')
def given_a_participant(step, username):
    world.participant = Participant.objects.get(username=username)

@step(r'When he uploads a submission to "(.*)"')
def when_uploads_submission(step, url):
    f = open("tests/test_submission.py", "r")
    submission = client.encode_file(client.MULTIPART_CONTENT, 'File', f) 
    f.close()

    response = world.browser.post(url, {'submission': submission,
                                        'participant': world.participant.id})
    assert response.status == 200
