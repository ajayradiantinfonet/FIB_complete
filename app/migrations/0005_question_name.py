# Generated by Django 3.2.3 on 2021-05-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210520_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
