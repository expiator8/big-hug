# Generated by Django 3.2.4 on 2021-06-05 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_post_types_post_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='country',
        ),
    ]