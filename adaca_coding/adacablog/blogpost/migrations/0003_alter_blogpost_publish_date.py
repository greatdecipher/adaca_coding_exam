# Generated by Django 4.2.5 on 2023-09-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_alter_blogpost_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
