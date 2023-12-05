# Generated by Django 4.2.6 on 2023-12-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eclass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userclasses', models.ManyToManyField(to='eclass.userclasslist')),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eclass.userprofile')),
            ],
        ),
    ]