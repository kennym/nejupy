from django.contrib import admin

from competition.models import Competition

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_time', 'end_time', 'status')
admin.site.register(Competition, CompetitionAdmin)

