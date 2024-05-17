# Generated by Django 5.0.6 on 2024-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maternal_entry', '0007_maternalentry_lack_of_transport_from_home_to_facility_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maternalentry',
            name='potential_avoidable_factors',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='maternalentry',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='maternalentry',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='maternalentry',
            name='dob_unknown',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='maternalentry',
            name='other_occupation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
