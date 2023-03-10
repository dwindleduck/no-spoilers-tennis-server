# Generated by Django 4.1 on 2023-03-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0002_watchedmatch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchedmatch',
            old_name='match_id',
            new_name='match',
        ),
        migrations.RenameField(
            model_name='watchedmatch',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
