# Generated by Django 4.1.3 on 2022-11-28 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bankingapp', '0004_services'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]