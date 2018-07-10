# Generated by Django 2.0.6 on 2018-06-29 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20180628_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.AlterField(
            model_name='login',
            name='roles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
