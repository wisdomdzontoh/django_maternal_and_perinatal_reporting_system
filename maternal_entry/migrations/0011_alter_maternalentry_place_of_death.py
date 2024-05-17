# Generated by Django 5.0.6 on 2024-05-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maternal_entry', '0010_alter_maternalentry_birth_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maternalentry',
            name='place_of_death',
            field=models.CharField(choices=[('teaching hospital', 'Teaching Hospital'), ('regional hospital', 'Regional Hospital'), ('district hospital', 'District Hospital'), ('polyclinic', 'Polyclinic'), ('health centre', 'Health Centre'), ('clinic', 'Clinic'), ('CHPS compound', 'CHPS Compound'), ('private maternity home', 'Private Maternity Home'), ('home', 'Home'), ('others (specify)', 'Others (Specify)')], default='none', max_length=100),
        ),
    ]
