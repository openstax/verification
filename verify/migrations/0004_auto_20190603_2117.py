# Generated by Django 2.0.9 on 2019-06-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0003_auto_20190521_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='verification',
            name='salesforce_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verification',
            name='faculty_email_address',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='ox_accounts_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='verification',
            name='school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='verification',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='verification',
            unique_together={('ox_accounts_id', 'salesforce_id')},
        ),
    ]