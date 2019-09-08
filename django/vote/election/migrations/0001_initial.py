# Generated by Django 2.0.7 on 2019-08-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.CharField(blank=True, max_length=255, null=True)),
                ('end_time', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
