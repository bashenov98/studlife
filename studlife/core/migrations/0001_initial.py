<<<<<<< HEAD
# Generated by Django 3.0.5 on 2020-04-26 19:31
=======
# Generated by Django 3.0.5 on 2020-04-26 21:28
>>>>>>> asd

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<< HEAD
        ('users', '0002_auto_20200426_1931'),
=======
        ('users', '0002_auto_20200426_2128'),
>>>>>>> asd
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='media/images', validators=[utils.validators.extension_validator, utils.validators.file_size_validator])),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
