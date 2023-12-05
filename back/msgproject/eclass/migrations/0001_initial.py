# Generated by Django 4.2.6 on 2023-12-04 13:52

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
            name='Classlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=20)),
                ('day1', models.CharField(blank=True, max_length=2, null=True)),
                ('day2', models.CharField(blank=True, max_length=2, null=True)),
                ('starttime1', models.CharField(blank=True, max_length=20, null=True)),
                ('endtime1', models.CharField(blank=True, max_length=20, null=True)),
                ('starttime2', models.CharField(blank=True, max_length=20, null=True)),
                ('endtime2', models.CharField(blank=True, max_length=20, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('major', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserClasslist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eclass.userprofile')),
                ('userclass', models.ManyToManyField(to='eclass.classlist')),
            ],
        ),
    ]
