# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random

@shared_task
def verify_sheerid(verification):
    request_success = '''{
    "firstName": "Randy",
    "lastName": "Random",
    "birthDate": "YYYY-MM-DD",
    "email": "name@example.com",
    "organization": {
        "id": 1,
        "name": "Organization name"
    }
    }'''

    request_doc_review = '''{
    "firstName": "REJECTED",
    "lastName": "Random",
    "birthDate": "YYYY-MM-DD",
    "email": "name@example.com",
    "organization": {
        "id": 1,
        "name": "Organization name"
    }
    }
    '''

    return random.choice([True, False])
