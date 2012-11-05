from django.utils.translation import ugettext_lazy as _
from django.db import models

class AuthToken(models.Model):
    user_id = models.CharField(max_length=50)
    session_id = models.CharField(max_length=255)
    token = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s %s %s" % (self.user_id, self.session_id, self.token, self.created)
