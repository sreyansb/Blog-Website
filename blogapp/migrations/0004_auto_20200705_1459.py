# Generated by Django 3.0.7 on 2020-07-05 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_post_sluf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sluf',
            new_name='slug',
        ),
    ]
