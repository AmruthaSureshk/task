# Generated by Django 3.2.12 on 2022-02-09 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='team_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='app1.users'),
            preserve_default=False,
        ),
    ]