# Generated by Django 2.2.7 on 2019-12-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodblog', '0002_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default='set.jpg', upload_to='images/'),
        ),
    ]
