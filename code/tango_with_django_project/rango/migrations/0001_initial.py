# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=180)),
                ('uid', models.CharField(default=uuid.uuid4, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('media_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rango.Media')),
                ('numPlays', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=('rango.media',),
        ),
        migrations.CreateModel(
            name='SheetMusic',
            fields=[
                ('media_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rango.Media')),
                ('instrument', models.CharField(max_length=180)),
                ('key', models.CharField(max_length=180)),
            ],
            options={
            },
            bases=('rango.media',),
        ),
        migrations.CreateModel(
            name='StreamModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sortBy', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Newest'), (b'1', b'Featured')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('media_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rango.Media')),
                ('type', models.CharField(default=b'0', max_length=180, choices=[(b'0', b'Chords'), (b'1', b'Tabs')])),
                ('key', models.CharField(max_length=180)),
            ],
            options={
            },
            bases=('rango.media',),
        ),
        migrations.CreateModel(
            name='verifiable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('verifiable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rango.verifiable')),
                ('website', models.URLField(blank=True)),
            ],
            options={
            },
            bases=('rango.verifiable',),
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('profile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rango.Profile')),
            ],
            options={
            },
            bases=('rango.profile',),
        ),
        migrations.CreateModel(
            name='GarageModel',
            fields=[
                ('profile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rango.Profile')),
            ],
            options={
            },
            bases=('rango.profile',),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
