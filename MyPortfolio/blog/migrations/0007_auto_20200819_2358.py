# Generated by Django 3.0.3 on 2020-08-20 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='message',
        ),
    ]