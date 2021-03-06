# Generated by Django 3.1.7 on 2021-03-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.IntegerField()),
                ('client_image', models.CharField(max_length=255)),
                ('client_logo_image', models.CharField(max_length=255)),
                ('client_detail', models.TextField()),
                ('client_link', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_image1', models.CharField(max_length=255)),
                ('project_image2', models.CharField(max_length=255)),
                ('project_image3', models.CharField(max_length=255)),
                ('project_date', models.CharField(max_length=50)),
                ('project_detail', models.TextField()),
                ('project_name', models.CharField(max_length=50)),
                ('project_status', models.CharField(max_length=50)),
                ('project_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='contactForm',
        ),
    ]
