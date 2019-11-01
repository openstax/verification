from django.core.management.base import BaseCommand
from salesforce.salesforce import Salesforce
from verify.models import Verification

class Command(BaseCommand):
    help = "updates Errata records to use book name in a text field"

    def handle(self, *args, **options):
        with Salesforce() as sf:
            command = "SELECT Id, Accounts_ID__c, Faculty_Verified__C FROM Contact"
            response = sf.query(command)

            for record in response['records']:
                salesforce_id = record['Id']
                ox_account_id = record['Accounts_ID__c']
                faculty_status = record['Faculty_Verified__c']

                if ox_account_id:
                    verification, created = Verification.objects.get_or_create(salesforce_id=salesforce_id)
                    verification.ox_accounts_id = ox_account_id
                    verification.status = faculty_status

                    verification.save()

                    print("Verification created for {}".format(salesforce_id))


        print("User Status Updated!")
