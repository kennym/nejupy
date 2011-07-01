from django.conf import settings

from celery.task import task
from ideone import Ideone

from submission.models import Submission

@task
def get_ideone_result_for(submission_id):
    """ Get Ideone result for submission with `submission_id`. """
    try:
        submission = Submission.objects.get(pk=submission_id)
        i = Ideone(settings.IDEONE_USER,
                   settings.IDEONE_PASS)
        result = i.create_submission(submission.source_code.read(),
                                     language_id=submission.programming_language,
                                     private=True)
        submission.link = result["link"]
         
        details = i.submission_details(result['link'])

        submission.memory = details["memory"]
        submission.output = details["output"]
        submission.result = details["result"]
        submission.status = details["status"]
        submission.stderr = details["stderr"]
        submission.e_time = details["time"]
        submission.save(force_update=True)
    except Exception, e:
        raise e
