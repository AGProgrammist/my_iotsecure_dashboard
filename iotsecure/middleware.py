from django.conf import settings
from datetime import datetime
from django.contrib import auth

class AutoLogout:
    def __init__(self, get_response):
        pass
    def process_request(self, request):
        if not request.user.is_authenticated():
            return
        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass
        request.session['last_touch'] = datetime.now()
