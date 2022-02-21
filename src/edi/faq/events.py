from datetime import datetime
from plone import api as ploneapi

def create_title(obj, event):
    now = datetime.now().strftime("%d.%m.%Y")
    user = ''
    if not ploneapi.user.is_anonymous():
        user = ploneapi.user.get_current().getProperty('fullname')
    obj.title = f"Antwort von {user} vom {now}"
