# Generated by Django 2.0.6 on 2018-06-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_auto_20180629_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role_permission',
            name='permission_name',
            field=models.CharField(default='employee', max_length=50),
        ),
    ]