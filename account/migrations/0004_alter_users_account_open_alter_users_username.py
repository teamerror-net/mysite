# Generated by Django 4.1.7 on 2023-03-30 23:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_users_absent_users_present'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='account_open',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Account Open'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(editable=False, max_length=20, unique=True, verbose_name='Username'),
        ),
    ]
