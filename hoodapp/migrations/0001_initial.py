# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-29 21:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('location', models.CharField(choices=[('Baringo', 'Baringo County'), ('Bomet', 'Bomet County'), ('Bungoma', 'Bungoma County'), ('Busia', 'Busia County'), ('Elgeyo Marakwet', 'Elgeyo Marakwet County'), ('Embu', 'Embu County'), ('Garissa', 'Garissa County'), ('Homa Bay', 'Homa Bay County'), ('Isiolo', 'Isiolo County'), ('Kajiado', 'Kajiado County'), ('Kakamega', 'Kakamega County'), ('Kericho', 'Kericho County'), ('Kiambu', 'Kiambu County'), ('Kilifi', 'Kilifi County'), ('Kirinyaga', 'Kirinyaga County'), ('Kisii', 'Kisii County'), ('Kisumu', 'Kisumu County'), ('Kitui', 'Kitui County'), ('Kwale', 'Kwale County'), ('Laikipia', 'Laikipia County'), ('Lamu', 'Lamu County'), ('Machakos', 'Machakos County'), ('Makueni', 'Makueni County'), ('Mandera', 'Mandera County'), ('Meru', 'Meru County'), ('Migori', 'Migori County'), ('Marsabit', 'Marsabit County'), ('Mombasa', 'Mombasa County'), ('Muranga', 'Muranga County'), ('Nairobi', 'Nairobi County'), ('Nakuru', 'Nakuru County'), ('Nandi', 'Nandi County'), ('Narok', 'Narok County'), ('Nyamira', 'Nyamira County'), ('Nyandarua', 'Nyandarua County'), ('Nyeri', 'Nyeri County'), ('Samburu', 'Samburu County'), ('Siaya', 'Siaya County'), ('Taita Taveta', 'Taita Taveta County'), ('Tana River', 'Tana River County'), ('Tharaka Nithi', 'Tharaka Nithi County'), ('Trans Nzoia', 'Trans Nzoia County'), ('Turkana', 'Turkana County'), ('Uasin Gishu', 'Uasin Gishu County'), ('Vihiga', 'Vihiga County'), ('Wajir', 'Wajir County'), ('West Pokot', 'West Pokot County')], max_length=100)),
                ('population', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.Neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='Awesome bio will appear here', max_length=500)),
                ('hood', models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='hoodapp.Neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='join',
            name='hood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='join',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
