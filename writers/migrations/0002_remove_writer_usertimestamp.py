# Generated by Django 4.2.5 on 2023-11-28 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='userTimeStamp',
        ),
    ]
