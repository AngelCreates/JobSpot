import ckeditor.fields
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
            name='FilledJobModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=1000, null=True)),
                ('job', models.CharField(blank=True, max_length=1000, null=True)),
                ('feedback', models.CharField(
                    blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('job_title', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), (
                    'Part Time', 'Part Time'), ('Intern', 'Intern')], max_length=30, null=True)),
                ('vacancy', models.CharField(blank=True, max_length=255, null=True)),
                ('responsibilities', ckeditor.fields.RichTextField(
                    blank=True, null=True)),
                ('requirements', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[
                 ('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], max_length=30, null=True)),
                ('job_desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('additional_note', ckeditor.fields.RichTextField(
                    blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='AppliedJobModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(
                    blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='job.jobmodel')),
            ],
        ),
    ]
