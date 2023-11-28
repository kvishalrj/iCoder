# Generated by Django 4.2.5 on 2023-11-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('bio', models.CharField(default='', max_length=1000)),
                ('userImage', models.ImageField(default='static/img/default.jpg', upload_to='static/img')),
                ('userTimeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
