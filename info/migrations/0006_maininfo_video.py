# Generated by Django 4.2.4 on 2024-03-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_award_news_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='maininfo',
            name='video',
            field=models.URLField(null=True, verbose_name='Introduction Video'),
        ),
    ]
