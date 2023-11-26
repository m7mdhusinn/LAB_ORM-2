# Generated by Django 4.2.7 on 2023-11-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='category',
            field=models.CharField(choices=[('Action', 'Action'), ('Drama', 'Drama'), ('Horro', 'Horro'), ('Fantasy', 'Fantasy')], default='Action', max_length=64),
        ),
        migrations.AddField(
            model_name='info',
            name='poster',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]