# Generated by Django 3.2.6 on 2021-08-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=15)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
