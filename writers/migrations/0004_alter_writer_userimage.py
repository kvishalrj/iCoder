# Generated by Django 4.2.5 on 2023-11-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0003_alter_writer_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='userImage',
            field=models.ImageField(default='static/img/default.jpg', upload_to='blog/user'),
        ),
    ]
