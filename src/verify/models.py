from django.db import models


STATUS_CHOICES = (
    ('no_faculty_info', 'No Faculty Info'),
    ('pending_faculty', 'Pending Faculty'),
    ('confirmed_faculty', 'Confirmed Faculty'),
    ('rejected_faculty', 'Rejected Faculty'),
)


class Verification(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    faculty_email_address = models.EmailField(unique=True)
    ox_accounts_id = models.IntegerField(unique=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='no_faculty_info')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.faculty_email_address