# Generated by Django 4.2.4 on 2024-02-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_teammember_facebook_teammember_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerimage',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='headerimage',
            name='description_ar',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='headerimage',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='headerimage',
            name='title',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='headerimage',
            name='title_ar',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='headerimage',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
    ]
