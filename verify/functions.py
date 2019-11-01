import json
from urllib.parse import urlencode
from urllib.request import urlopen
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from django.conf import settings

def get_token():
    """
    """
    client = BackendApplicationClient(client_id=settings.SOCIAL_AUTH_OPENSTAX_KEY)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=settings.ACCESS_TOKEN_URL,
                              client_id=settings.SOCIAL_AUTH_OPENSTAX_KEY,
                              client_secret=settings.SOCIAL_AUTH_OPENSTAX_SECRET)

    return token

def get_user_info(uid):
    """
    """
    if uid:
        token = get_token()
        url = settings.USERS_QUERY + urlencode({
            'q': 'id:{}'.format(uid),
            'access_token': token['access_token']
        })

        with urlopen(url) as url:
            data = json.loads(url.read().decode())

            # update email address if possible
            try:
                contact_infos = data['items'][0]['contact_infos']
                most_recent_email = max(contact_infos, key=lambda x: x['id'])
                email = most_recent_email['value']
            except (ValueError, IndexError):
                email = None  # no saved emails

            # update full name if possible
            try: 
                fullname = data['items'][0]['full_name']
            except (ValueError, IndexError):
                fullname = None

            user_data = {
                'email': email,
                'fullname': fullname
            }

            return user_data
    else:
        return False