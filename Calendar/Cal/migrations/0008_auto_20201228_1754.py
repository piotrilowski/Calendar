# Generated by Django 3.1.3 on 2020-12-28 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cal', '0007_auto_20201228_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmember',
            name='action',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='eventmember',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]