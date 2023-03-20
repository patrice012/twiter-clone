# Generated by Django 3.2.16 on 2023-03-11 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profil.utils
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('profil_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Profil name')),
                ('profil_picture', models.ImageField(blank=True, null=True, upload_to=profil.utils.user_diresctory, verbose_name='Picture')),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to=profil.utils.user_diresctory, verbose_name='Cover picture')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Say more about you.')),
                ('about', tinymce.models.HTMLField()),
                ('location', models.CharField(max_length=50, verbose_name='Your current location')),
                ('career', models.CharField(max_length=50, verbose_name='Your career')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name="You're social link")),
                ('link_name', models.CharField(max_length=50, verbose_name='Social app name')),
                ('for_profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='profil.profil')),
            ],
        ),
    ]
