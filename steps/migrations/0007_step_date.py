# Generated by Django 3.1.7 on 2021-06-08 20:07

from django.db import migrations, models
import django.forms.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0006_remove_step_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='date',
            field=models.DateField(default='2021-06-08'),
        ),
    ]
