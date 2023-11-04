# Generated by Django 4.2.7 on 2023-11-04 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eclass', '0004_userprofile_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_title', models.CharField(max_length=100)),
                ('in_startdate', models.DateField()),
                ('in_enddate', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eclass.userprofile')),
            ],
        ),
    ]