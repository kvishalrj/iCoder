# Generated by Django 4.1.13 on 2024-02-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.CharField(default='/static/img/blog.png', max_length=1000),
        ),
    ]
