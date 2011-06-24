from django.contrib import admin

from submission.models import Submission

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'participant', 'problem', 'source_code')
admin.site.register(Submission, SubmissionAdmin)

