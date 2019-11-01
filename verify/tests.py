import json
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import RequestsClient, APIRequestFactory, force_authenticate, APITestCase
from django.contrib.auth import get_user_model

from verify.models import Verification


class VerifyTest(APITestCase):
    def test_can_add_verification(self):
        response = self.client.post('/api/verify/', {'ox_accounts_id': 1599})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Verification.objects.count(), 1)
        self.assertEqual(Verification.objects.get().ox_accounts_id, 1599)

    def test_new_verification_not_verified(self):
        response = self.client.post('/api/verify/', {'ox_accounts_id': 1599})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/api/verify/?ox_accounts_id=1599')
        self.assertEqual(json.loads(response.content)["results"][0]["status"], None)

    def test_query_returns_only_one_response(self):
        response = self.client.post('/api/verify/', {'ox_accounts_id': 1599})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/api/verify/?ox_accounts_id=1599')
        self.assertEqual(json.loads(response.content)["count"], 1)

    def test_can_retrieve_verification(self):
        response = self.client.post('/api/verify/', {'ox_accounts_id': 1547})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        verification = Verification.objects.get(ox_accounts_id=1547)

        # we are mocking up a successful verification
        verification.salesforce_id = '003U000001it9mXIAQ'
        verification.status = 'Confirmed'
        verification.save()

        response = self.client.get('/api/verify/{}/'.format(verification.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'id': verification.id,
                                                        'salesforce_id': '003U000001it9mXIAQ',
                                                        'ox_accounts_id': 1547,
                                                        'status': 'Confirmed',
                                                        'created': verification.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                                                        'modified': verification.modified.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                                                        'accounts_info': False})
