from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.models import User

def get_current_user():

    user_id = []
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())

    for session in active_sessions:
        data = session.get_decoded()
        user_id.append(data.get('_auth_user_id', None))
    user = User.objects.get(id=user_id[0])

    return user