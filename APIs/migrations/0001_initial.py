# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:03
from __future__ import unicode_literals

import APIs.validators.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('src_path', models.CharField(max_length=250, verbose_name='Path')),
                ('event_type', models.CharField(max_length=200, verbose_name='Evenet type')),
                ('md5sum', models.CharField(blank=True, max_length=50, null=True, verbose_name='MD5')),
                ('sha256sum', models.CharField(blank=True, max_length=256, null=True, verbose_name='SHA256')),
                ('filesize', models.CharField(blank=True, max_length=50, null=True, verbose_name='File size')),
                ('fileType', models.CharField(blank=True, max_length=100, null=True, verbose_name='File type')),
                ('fileExtension', models.CharField(blank=True, max_length=50, null=True, verbose_name='File extension')),
                ('fileContent', models.TextField(blank=True, null=True, verbose_name='File content')),
                ('wasSeenBefore', models.BooleanField(default=False, verbose_name='Was seen before')),
                ('is_malicious', models.BooleanField(default=False, verbose_name='Is malicious')),
                ('yara_tags', models.CharField(blank=True, max_length=50, null=True, verbose_name='Yara tags')),
                ('yara_patterns', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Hit',
                'verbose_name_plural': 'Hits',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Tag name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='WatcherConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('server_name', models.CharField(help_text='This is an identifier for the mount you want to monitor.<br />Example: <b>OWA-Server1</b>.', max_length=50, unique=True, verbose_name='Server name')),
                ('share_path', models.CharField(help_text='An absolute path for the directory you want to monitor.<br />Exampe: <b>/mnt/OWAServer1</b>.', max_length=250, unique=True, validators=[APIs.validators.validators.validate_share_path], verbose_name='Share path')),
                ('patterns', models.CharField(help_text='List of the patterns that need to be monitored within the share path.<br />Exampe: <b>*.aspx,*.dll,*.dll</b>.', max_length=200, verbose_name='Patterns')),
                ('ignored_patterns', models.CharField(blank=True, help_text="List of the patterns you may ignore incase the patterns field is set to match all files '*.*'.", max_length=200, null=True, verbose_name='Ignored patterns')),
                ('comment', models.TextField(blank=True)),
                ('allow_alerting', models.BooleanField(default=True, help_text='Send an email alert when an event triggers.', verbose_name='Send email alerts')),
                ('is_up', models.BooleanField(default=False, help_text='The watcher status (up/down).')),
                ('exception', models.TextField(blank=True, help_text='The exception that mad the watcher to stop.', null=True)),
                ('needs_restart', models.BooleanField(default=False, help_text='Restart the watcher incase of an exception.')),
                ('tags', models.ManyToManyField(blank=True, to='APIs.Tag')),
            ],
            options={
                'verbose_name': 'Watcher',
                'verbose_name_plural': 'Watchers',
            },
        ),
        migrations.AddField(
            model_name='hit',
            name='watcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIs.WatcherConfig'),
        ),
    ]