# Generated by Django 2.2.7 on 2019-12-20 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodblog', '0007_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='u_id',
            new_name='uid',
        ),
    ]
