# Generated by Django 3.1.6 on 2021-05-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210514_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(default=False, max_length=30, unique=True),
        ),
    ]
