# Generated by Django 4.2.5 on 2023-11-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postImage',
            field=models.ImageField(default='static/img/default.jpg', upload_to='static/img'),
        ),
    ]
