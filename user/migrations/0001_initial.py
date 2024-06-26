import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_applicant', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('about', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('totalViewCount', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperienceModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), (
                    'Part Time', 'Part Time'), ('Intern', 'Intern')], max_length=30, null=True)),
                ('job_desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('company', models.CharField(default='nazia', max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('started', models.DateField(blank=True, null=True)),
                ('left', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillSetModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('proficiency', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), (
                    'Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Pro', 'Pro')], max_length=255, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('workplace', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(default='', max_length=255)),
                ('extra', models.CharField(default=0, max_length=255)),
                ('rate', models.IntegerField(default=0, validators=[
                 django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('applicant', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='user.companyprofilemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileViewDetails',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('viewed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='viewed', to=settings.AUTH_USER_MODEL)),
                ('viewedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='viewedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreferredJobModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('proficiency', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), (
                    'Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Native', 'Native')], max_length=30, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobSearchKeywordModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('searched_for', models.CharField(
                    blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('searched_by', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSearchKeywordModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('searched_for', models.CharField(
                    blank=True, max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('searched_by', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(
                    blank=True, max_length=255, null=True)),
                ('started', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('cgpa', models.FloatField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AwardModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[
                 ('Male', 'Male'), ('Female', 'Female')], max_length=255, null=True)),
                ('interest', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='')),
                ('totalViewCount', models.IntegerField(
                    blank=True, default=0, null=True)),
                ('user', models.OneToOneField(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
