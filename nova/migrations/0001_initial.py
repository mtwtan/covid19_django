# Generated by Django 3.0.8 on 2020-07-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'counties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DmvMovingAverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(blank=True, null=True)),
                ('county', models.TextField(blank=True, null=True)),
                ('numconfirmed', models.BigIntegerField(blank=True, db_column='numConfirmed', null=True)),
                ('numdeaths', models.BigIntegerField(blank=True, db_column='numDeaths', null=True)),
                ('daybefore', models.BigIntegerField(blank=True, db_column='dayBefore', null=True)),
                ('change', models.BigIntegerField(blank=True, null=True)),
                ('daybeforedeaths', models.BigIntegerField(blank=True, db_column='dayBeforeDeaths', null=True)),
                ('changedeaths', models.BigIntegerField(blank=True, db_column='changeDeaths', null=True)),
                ('movingaverage', models.FloatField(blank=True, db_column='movingAverage', null=True)),
                ('movingaveragedeaths', models.FloatField(db_column='movingAverageDeaths')),
            ],
            options={
                'db_table': 'dmv_moving_average',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Testcovid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('confirmed', models.IntegerField()),
                ('death', models.IntegerField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'testcovid',
                'managed': False,
            },
        ),
    ]
