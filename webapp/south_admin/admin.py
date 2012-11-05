from django.contrib import admin
from south.models import MigrationHistory

class MigrationHistoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(MigrationHistory, MigrationHistoryAdmin)