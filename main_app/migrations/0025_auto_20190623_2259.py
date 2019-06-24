# Generated by Django 2.2 on 2019-06-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_auto_20190623_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='effects',
            field=models.ManyToManyField(through='main_app.User_Drug_Effects', to='main_app.Effect'),
        ),
        migrations.AlterField(
            model_name='trip_report',
            name='effects',
            field=models.ManyToManyField(to='main_app.User_Drug_Effects'),
        ),
    ]