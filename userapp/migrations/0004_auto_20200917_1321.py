# Generated by Django 2.2.10 on 2020-09-17 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_auto_20200917_1320'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='userapp_address',
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='userapp_userinfo',
        ),
    ]