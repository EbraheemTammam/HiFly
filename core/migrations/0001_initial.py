# Generated by Django 4.1.7 on 2023-03-31 14:22

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=10)),
                ('social_status', models.CharField(max_length=10)),
                ('degree', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('national_id', models.CharField(max_length=14)),
                ('governorate', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=13)),
                ('dad_phone_number', models.CharField(max_length=13)),
                ('mom_phone_number', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
            ],
            bases=('core.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
                ('level', models.IntegerField()),
                ('semester', models.IntegerField()),
            ],
            bases=('core.person',),
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=core.models.effect_upload_path)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='effects', to='core.person')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=core.models.attachment_upload_path)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='core.person')),
            ],
        ),
    ]
