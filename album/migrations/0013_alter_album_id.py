# Generated by Django 5.0.6 on 2024-06-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0012_rename_albums_album_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
