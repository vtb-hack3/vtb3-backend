# Generated by Django 3.2.8 on 2021-10-10 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('id',)},
        ),
    ]
