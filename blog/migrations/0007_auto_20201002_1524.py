# Generated by Django 3.0.8 on 2020-10-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200716_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.CharField(default='comment', max_length=100),
        ),
    ]