# Generated by Django 2.2.10 on 2020-09-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_address_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=40, null=True)),
            ],
            options={
                'db_table': 'areas',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'managed': False},
        ),
    ]
