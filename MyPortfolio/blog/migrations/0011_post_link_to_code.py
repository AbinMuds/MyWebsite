# Generated by Django 3.0.3 on 2020-08-24 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link_to_code',
            field=models.URLField(blank=True),
        ),
    ]
