# Generated by Django 3.0.8 on 2020-07-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=11)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('designation', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'recruiter_companyinsert',
            },
        ),
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('mobile_number', models.CharField(default='', max_length=11)),
                ('message', models.TextField(default='', max_length=50)),
            ],
            options={
                'db_table': 'recruiter_demo',
            },
        ),
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=50)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('job_type', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=100)),
                ('job_description', models.TextField(default='', max_length=100)),
                ('qualifications', models.TextField(default='', max_length=100)),
                ('additional_info', models.TextField(default='', max_length=200)),
            ],
            options={
                'db_table': 'recruiter_jobinsert',
            },
        ),
        migrations.CreateModel(
            name='UserInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default='', max_length=100)),
                ('LastName', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=100)),
                ('PhoneNumber', models.CharField(default='', max_length=11)),
                ('Address', models.CharField(default='', max_length=100)),
                ('document', models.FileField(default='', upload_to='media/%Y/%m/%d')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='UserResumes',
            fields=[
                ('Resume_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=100)),
                ('mobile', models.CharField(default='', max_length=11)),
                ('email', models.CharField(default='', max_length=50)),
                ('skills', models.CharField(default='', max_length=500)),
                ('company', models.CharField(blank=True, max_length=500, null=True)),
                ('experience', models.TextField(blank=True, max_length=1000, null=True)),
                ('experience_in_year', models.CharField(blank=True, max_length=5, null=True)),
                ('designation', models.TextField(blank=True, max_length=500, null=True)),
                ('college_name', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'resumeparser',
            },
        ),
    ]
