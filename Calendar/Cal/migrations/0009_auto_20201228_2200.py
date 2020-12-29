# Generated by Django 3.1.3 on 2020-12-28 21:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cal', '0008_auto_20201228_1754'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventmember',
            unique_together={('event', 'user', 'email', 'action')},
        ),
    ]
