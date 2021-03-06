# Generated by Django 3.0.5 on 2020-04-26 13:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'max_length': 'Too many characters', 'unique': 'This username is already taken'}, max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last_name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_student', models.BooleanField(default=False, verbose_name='student status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images', validators=[utils.validators.extension_validator, utils.validators.file_size_validator])),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/images', validators=[utils.validators.extension_validator, utils.validators.file_size_validator])),
                ('bio', models.TextField(max_length=500)),
                ('faculty', models.PositiveSmallIntegerField(choices=[(0, 'FACULTY OF INFORMATION TECHNOLOGIES'), (1, 'INTERNATIONAL SCHOOL OF ECONOMICS'), (2, 'BUSINESS SCHOOL'), (3, 'KAZAKHSTAN MARITIME ACADEMY'), (4, 'SCHOOL OF MATHEMATICS AND CYBERNETICS'), (5, 'SCHOOL OF CHEMICAL ENGINEERING'), (6, 'FACULTY OF GEOLOGY AND EXPLORATION'), (7, 'FACULTY OF ENERGY AND OIL ANG GAS INDUSTRY')], default=0)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
