# Generated by Django 2.2.2 on 2019-06-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20190622_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripreportphoto',
            old_name='trip_report',
            new_name='trip_report_key',
        ),
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