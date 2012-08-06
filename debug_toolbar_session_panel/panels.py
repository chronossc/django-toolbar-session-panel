# -*- coding: utf-8 -*-
from debug_toolbar.panels import DebugPanel 
from django.utils.translation import ugettext_lazy as _
from django.utils.datastructures import SortedDict

class SessionDebugPanel(DebugPanel):
    """
    Panel that displays session content
    """
    name = 'Session'
    template = 'debug_toolbar_session_panel/panel.html'
    has_content = True

    def nav_title(self):
        return _('Session')

    def title(self):
        return self.nav_title()

    def url(self):
        return ''

    def process_response(self, request, response):
        data = {'session':{
            'info': SortedDict([
                ('session_key',request.session.session_key),
                ('user', request._cached_user),
                ('modified', request.session.modified),
                ('accessed', request.session.accessed)
                ]),
            'data': dict(request.session.items())
        }}
        self.record_stats(data)
