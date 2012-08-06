# Session Debug Panel

This panel allow you to query your session after request.

## Install

With pip:

    pip install -e git+git://github.com/chronossc/django-toolbar-session-panel.git#egg=debug_toolbar_session_panel

and in settings.py:

    INSTALLED_APPS += (
        'debug_toolbar_session_panel',
    )
    DEBUG_TOOLBAR_PANELS += (
        'debug_toolbar_session_panel.panels.SessionDebugPanel',
    )

than you will see something like:

<img src="http://chronosbox.org/screenshots/session_demo.png" />