import logging
import uuid

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from djangorestframework.views import View
from djangorestframework.response import Response
from djangorestframework import status
from djangorestframework.utils import MSIE_USER_AGENT_REGEX

from exceptions import *
from forms import *
from models import *

logger = logging.getLogger('webapp')


class FixIEView(View):
    _IGNORE_IE_ACCEPT_HEADER = False

#    def _load_method_and_content_type(self):
#        super(FixIEView, self)._load_method_and_content_type()
#        try:
#            #fix stupid IE8/9 bug that causes it to be unable to pick an intelligent content-type header
#            if self._content_type in ['', 'text/plain'] and self.request and 'HTTP_USER_AGENT' in self.request.META and MSIE_USER_AGENT_REGEX.match(self.request.META['HTTP_USER_AGENT']):
#                self._method = 'POST'
#                self._content_type = 'application/x-www-form-urlencoded'
#                logger.info('Fixed IE content-type to %s' % self._content_type)
#        except:
#            pass

class BeginSessionView(FixIEView):

    form = BeginSessionViewForm

    def post(self, request):

        #Step 0: verify params
        data = self.CONTENT

        auth_user_id = data.get('auth_user_id')
        session_id = data.get('session_id')

        #Step 1: authenticate
        # do something fancy here


        #Step 2: client authenticated; reuse existing OR generate token for further communication
        try:
            auth_token = AuthToken.objects.get(user_id=auth_user_id, session_id=session_id).token
        except ObjectDoesNotExist:
            auth_token = uuid.uuid4()
            AuthToken.objects.create(user_id=auth_user_id, session_id=session_id, token=auth_token)

        #Step3: return token and userId for caller to use
        return {"auth_user_id": auth_user_id, "auth_token": auth_token}

