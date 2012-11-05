
from djangorestframework import status
from djangorestframework.response import ErrorResponse


class UnauthorizedException(ErrorResponse):
    def __init__(self, *args, **kwargs):
        super(UnauthorizedException, self).__init__(status.HTTP_401_UNAUTHORIZED, content={'ERROR': 'Unauthorized request.'}, *args, **kwargs)


class DoesNotExistException(ErrorResponse):
    def __init__(self, content=None, headers={}):
        #NOTE: because of XHR limitations, IE8/9 does not see anything but "500:error"
        #even if you send more content and data. Which means we can't use ErrorResponse
        #for communicating anything meaningful unless we send a 200 status. *sigh*
        super(DoesNotExistException, self).__init__(status.HTTP_200_OK, content=content, headers=headers)
