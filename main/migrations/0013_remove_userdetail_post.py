# Generated by Django 4.0.2 on 2022-04-25 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_post_image_userdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='post',
        ),
    ]
