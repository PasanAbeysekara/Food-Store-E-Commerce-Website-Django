# Generated by Django 3.2.3 on 2021-06-02 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='lname',
            new_name='last_name',
        ),
    ]
