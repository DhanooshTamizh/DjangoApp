# Generated by Django 3.0.7 on 2020-07-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='git_link',
            field=models.CharField(default='github', max_length=50),
        ),
    ]
