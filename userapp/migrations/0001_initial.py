# Generated by Django 2.2.10 on 2020-09-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('areaid', models.IntegerField(primary_key=True, serialize=False)),
                ('areaname', models.CharField(max_length=50)),
                ('parentid', models.IntegerField()),
                ('arealevel', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'area',
            },
        ),
    ]