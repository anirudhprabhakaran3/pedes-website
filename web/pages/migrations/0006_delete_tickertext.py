# Generated by Django 5.0.3 on 2024-08-28 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_tickertext_is_active_alter_tickertext_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TickerText',
        ),
    ]
