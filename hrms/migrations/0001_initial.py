# Generated by Django 4.2.1 on 2023-05-23 18:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(default='location', max_length=70)),
                ('history', models.TextField(blank=True, default='No History', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(default='emp778', max_length=70)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(default='Job Title', max_length=20)),
                ('dob', models.DateTimeField()),
                ('mobile', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=125)),
                ('address', models.TextField(default='', max_length=100)),
                ('emergency', models.CharField(max_length=11)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('luganda', 'LUGANDA')], default='english', max_length=10)),
                ('account_no', models.CharField(default='0123456789', max_length=10)),
                ('bank', models.CharField(default='First Bank Plc', max_length=25)),
                ('salary', models.CharField(default='00,000.00', max_length=16)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.department')),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=25)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(default='avatar.jpg', upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_period_start', models.DateField()),
                ('pay_period_end', models.DateField()),
                ('gross_pay', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deductions', models.DecimalField(decimal_places=2, max_digits=8)),
                ('net_pay', models.DecimalField(decimal_places=2, max_digits=8)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=15)),
                ('end', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('unapproved', 'UNAPPROVED'), ('decline', 'DECLINED')], default='Not Approved', max_length=15)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Kin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('occupation', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=14)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('first_in', models.TimeField()),
                ('last_out', models.TimeField(null=True)),
                ('status', models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('UNAVAILABLE', 'UNAVAILABLE')], max_length=15)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.employee')),
            ],
        ),
    ]
