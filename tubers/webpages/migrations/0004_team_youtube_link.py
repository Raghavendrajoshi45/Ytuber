# Generated by Django 3.1.6 on 2021-02-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
