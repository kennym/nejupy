from django.contrib import admin

from judge.models import Judge

class JudgeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'competition',)
admin.site.register(Judge, JudgeAdmin)

