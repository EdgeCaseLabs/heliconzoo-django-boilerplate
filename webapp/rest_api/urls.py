from django.conf.urls.defaults import *

from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

from .views import *

urlpatterns = patterns('',
    url(r'^/BeginSession$', BeginSessionView.as_view()),
)