# Generated by Django 2.2.2 on 2019-06-17 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190617_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Drug')),
            ],
        ),
    ]