# Generated by Django 3.1.3 on 2020-12-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cal', '0002_auto_20201223_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='data_pub',
            new_name='created_date',
        ),
    ]