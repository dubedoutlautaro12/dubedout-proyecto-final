# Generated by Django 4.1.3 on 2023-01-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo_2', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='posteos'),
        ),
    ]
