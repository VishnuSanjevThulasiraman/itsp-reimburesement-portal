# Generated by Django 3.0.5 on 2020-04-12 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='team_name',
            new_name='title',
        ),
    ]