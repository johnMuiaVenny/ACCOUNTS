# Generated by Django 3.2.6 on 2021-08-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS2', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone',
            field=models.IntegerField(null=True),
        ),
    ]
