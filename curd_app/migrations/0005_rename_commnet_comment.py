# Generated by Django 3.2.3 on 2021-05-22 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curd_app', '0004_commnet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commnet',
            new_name='Comment',
        ),
    ]