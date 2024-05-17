# Generated by Django 5.0.6 on 2024-05-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maternal_entry', '0005_alter_maternalentry_identified_risk_factors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maternalentry',
            name='declined_treatment_admission',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont know', 'Dont Know')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='maternalentry',
            name='specify_declined_treatment_admission',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='maternalentry',
            name='primary_obstetric_COD',
            field=models.TextField(choices=[('haemorrhage', 'Haemorrhage'), ('unsafe abortion', 'Unsafe abortion'), ('ruptured uterus', 'Ruptured Uterus'), ('obstructed labour', 'Obstructed Labour'), ('malaria', 'Malaria'), ('hypertensive disease', 'hypertensive disease'), ('genital tract sepsis', 'Genital Tract Sepsis'), ('ectopic pregnancy', 'Ectopic Pregnancy'), ('sickle cell disease', 'Sickle Cell disease')], null=True),
        ),
    ]
