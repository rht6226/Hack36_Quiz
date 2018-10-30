# Generated by Django 2.0.2 on 2018-09-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20180922_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='code',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
