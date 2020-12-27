# Generated by Django 3.1.3 on 2020-12-23 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='active',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='data_pub',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='EventMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cal.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
    ]
