# Generated by Django 4.2 on 2024-08-30 10:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_car_title_alter_car_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle_interest', models.CharField(blank=True, max_length=255, null=True)),
                ('inquiry_type', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created_on',),
                'abstract': False,
            },
        ),
    ]
