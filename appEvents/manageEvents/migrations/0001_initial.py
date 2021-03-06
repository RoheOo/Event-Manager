# Generated by Django 4.0.4 on 2022-05-26 23:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('bussines_type', models.IntegerField(choices=[[0, 'Consult'], [1, 'Sugest'], [2, 'Others']])),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('event_description', models.TextField()),
                ('subscribe', models.ManyToManyField(blank=True, related_name='subscribe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
