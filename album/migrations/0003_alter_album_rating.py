# Generated by Django 5.0.6 on 2024-06-07 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Rating',
            field=models.CharField(choices=[(1, '1'), (4, '4'), (5, '5'), (2, '2'), (3, '3')], default=1, max_length=1),
        ),
    ]
