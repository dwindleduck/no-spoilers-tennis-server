# Generated by Django 4.1 on 2023-03-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0010_alter_watchedmatch_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchedmatch',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]
