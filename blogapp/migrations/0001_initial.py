# Generated by Django 3.0.7 on 2020-07-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
