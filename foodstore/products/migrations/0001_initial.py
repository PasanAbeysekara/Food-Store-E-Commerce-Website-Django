# Generated by Django 3.2.3 on 2021-06-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quentity', models.IntegerField()),
            ],
        ),
    ]