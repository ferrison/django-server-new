# Generated by Django 2.0.3 on 2018-04-09 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='id',
        ),
        migrations.AlterField(
            model_name='time',
            name='nom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='land.nom'),
        ),
    ]