from django.conf import settings

from celery.task import task
from ideone import Ideone

import urllib2


service = Ideone(settings.IDEONE_USER, settings.IDEONE_PASS)

@task(max_retries=3)
def create_ideone_submission(source_code, programming_language):
    result = service.create_submission(source_code,
                                 language_id=programming_language,
                                 private=True)
    return result

@task(max_retries=3)
def get_submission_details(link):
    """ Get Ideone submission details for `link`. """

    details = service.submission_details(link)

    data = {
        "link": link,
        "memory": details["memory"],
        "output": details["output"],
        "result": details["result"],
        "status": details["status"],
        "stderr": details["stderr"],
        "e_time": details["time"]
    }

    return data
