# Generated by Django 3.0.1 on 2020-02-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20200209_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]